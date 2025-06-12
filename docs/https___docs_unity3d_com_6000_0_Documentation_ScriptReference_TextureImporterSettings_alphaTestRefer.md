* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-alphaTestReferenceValue.html

#  [TextureImporterSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings.html).alphaTestReferenceValue
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
alphaTestReferenceValue; 
### Description
Returns or assigns the alpha test reference value.
Returns the reference value (also known as the alpha cutoff) used to compute values needed to preserve alpha mipmap coverage on textures. A pixel is considered to be completely transparent when this value is greater than or equal to the pixel's alpha value. Always match the alpha cutoff value used in the alpha test to avoid unexpected results.
* * *
