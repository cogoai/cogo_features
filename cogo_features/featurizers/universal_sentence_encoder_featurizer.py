from rasa_nlu.featurizers import Featurizer
from .cogo_features_client import fetch_feature_remotely

class UniversalSentenceEncoderFeaturizer(Featurizer):
    """Appends a universal sentence encoding to the message's text_features."""

    name = "universal_sentence_encoder_featurizer"

    # We don't require any previous pipline step and return text_features
    requires = []
    provides = ["text_features"]

    def __init__(self, component_config):
        super(UniversalSentenceEncoderFeaturizer, self).__init__(component_config)


    def train(self, training_data, config, **kwargs):
        # Nothing to train, just process all training examples so that the
        # feature is set for future pipeline steps
        from .local_encoder import LocalEncoder
        local_encoder = LocalEncoder()
        for example in training_data.training_examples:
            feature_vector = local_encoder.encode(example.text)
            features = self._combine_with_existing_text_features(example, feature_vector)
            example.set("text_features", features)


    def process(self, message, **kwargs):
        feature_vector = fetch_feature_remotely(message.text)
        # Concatenate the feature vector with any existing text features
        features = self._combine_with_existing_text_features(message, feature_vector)
        # Set the feature, overwriting any existing `text_features`
        message.set("text_features", features)

    @classmethod
    def load(cls, model_dir=None, model_metadata=None, cached_component=None,
             **kwargs):
        """Load this component from file."""

        if cached_component:
            return cached_component
        else:
            component_config = model_metadata.for_component(cls.name)
            return cls(component_config)
