* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.StripUnatlasedSpriteCopies.html

#  [BuildAssetBundleOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.html).StripUnatlasedSpriteCopies
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
### Description
Use to prevent duplicating a texture when it is referenced in multiple bundles. This would primarily happen with particle systems. The new behavior does not duplicate the texture if the sprite does not belong to an atlas. Using this flag is the desired behavior, but is not set by default for backwards compatability reasons.
* * *
