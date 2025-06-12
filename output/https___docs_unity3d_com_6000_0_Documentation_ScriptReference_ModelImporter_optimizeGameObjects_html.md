* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-optimizeGameObjects.html

#  [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).optimizeGameObjects
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
optimizeGameObjects; 
### Description
Animation optimization setting.
In the GameObjects hierarchy of a character, the GameObjects which only contain Transform component, will be optimized out unless they are specified in [extraExposedTransformPaths](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-extraExposedTransformPaths.html) for better CPU performance. The remaining GameObjects hierarchy will be flattened.
* * *
