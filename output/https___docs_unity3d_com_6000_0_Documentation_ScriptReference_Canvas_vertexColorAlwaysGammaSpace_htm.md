* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-vertexColorAlwaysGammaSpace.html

#  [Canvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html).vertexColorAlwaysGammaSpace
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
vertexColorAlwaysGammaSpace; 
### Description
Should the Canvas vertex color always be in gamma space before passing to the UI shaders in linear color space work flow.
Keeping the Canvas vertex color in gamma space will allow the gamma to linear conversion to happen in UI shaders, where colors have higher precision. This enhances UI color precision in linear color space workflow, especially for darker colors. Buit-in UI shaders include gamma to linear conversion. However, in custom UI shaders, user needs to provide gamma to linear conversion. 
* * *
