# GPT-4V samples

![Screenshot of GPT-4V conversations](./images/cover.png)

Samples for GPT-4V response curated by myself

[HF dataset](https://huggingface.co/datasets/theblackcat102/gpt-4v-eval-samples)

Some topics I am exploring:

1. Industry use : PCB design, defect detection in semicon

2. Anime, meme, abstract drawings

3. Animal or food recognition in captcha fashion

4. chart, flow chart, aws diagram, random drawings...

5. Wireframe, screenshot to code

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

The conversations should be in english (what GPT-4V best in) and focus in challenging what the vision section could extract and express it in text. So most questions should start with probing what the vision model can see.

I don't prefer asking any questions which requires language reasoning ( example:  give me ideas of XXX ) cause its already pretty good in the original GPT-4 model. But if your contribution is a good question then it should be a pass for me.

Currently due to limitation of huggingface dataset schema, only 1 image are allowed to pair with a conversations. So we had to work with this unless someone had a better proposal.
