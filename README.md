# Cogo Features
Sentences encoding infrastructure.

## Client
When a model is trained, a local pretrained model is used.

However, when a classification is processed, the featurizer calls the remote sentences encoding server to get the sentence embedding of a sentence.

**Please set the environment variables below** 

- TFHUB_URL
- COGO\_FEATURES\_SERVER_URL

Speficy the module in the rasa pipline configs file as below:

```
- name: "cogo_features.featurizers.UniversalSentenceEncoderFeaturizer"
```

## Server
In progress...
