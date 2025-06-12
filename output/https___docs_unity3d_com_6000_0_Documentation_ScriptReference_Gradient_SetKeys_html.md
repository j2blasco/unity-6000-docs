* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.SetKeys.html

#  [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html).SetKeys
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
## Declaration
public void SetKeys(GradientColorKey[] colorKeys, GradientAlphaKey[] alphaKeys); 
### Parameters
Parameter | Description  
---|---  
colorKeys | Color keys of the gradient (maximum 8 color keys).  
alphaKeys | Alpha keys of the gradient (maximum 8 alpha keys).  
### Description
Setup Gradient with an array of color keys and alpha keys.
Note that the alpha and colors keys will be automatically sorted by time value and that it is ensured to always have a minimum of 2 color keys and 2 alpha keys.
* * *
