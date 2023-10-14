# gpt-4v-samples
Samples for GPT-4V response curated by myself

[HF dataset](https://huggingface.co/datasets/theblackcat102/gpt-4v-eval-samples)

Some topics I am exploring:

1. PCB design

2. Defect detection in semicon

3. Anime, meme, abstract drawings

4. Animal or food recognition in captcha fashion

5. chart, flow chart, aws diagram...

6. Wireframe to code

## Some random conclusion:

1. The OCR ability is limited under english, for non-english languages its mostly just guessing.

2. Non english and vision alignment is still not very good, so I have sticked to english conversations for now.


## Contribution Guide

If you wish to contribute to this dataset, please submit a merge requests.

The format should be as follows:

```
data/
    unique image filename.jpg or png
    unique image filename.json
```

The json format should be as follows:

```
[
  {"human": "..."},
  {"gpt": "The response of GPT-4V"},
  ...
]
```

The conversations should be in english (what GPT-4V best in)

Currently due to limitation of huggingface dataset schema, only 1 image are allowed to pair with a conversations. So we had to work with this unless someone had a better proposal.
