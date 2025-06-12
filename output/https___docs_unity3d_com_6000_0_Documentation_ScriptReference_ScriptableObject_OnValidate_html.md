* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnValidate.html

#  [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html).OnValidate()
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html "Go to ScriptableObject Component in the Manual")
### Description
Editor-only function that Unity calls when the script is loaded or a value changes in the Inspector.
`OnValidate` is usually used to perform an action after a value changes in the Inspector. For example, making sure that data stays within a certain range.  
  
The following operations aren't supported and can cause errors in your application when performed from `OnValidate`: 
  * Modifying values on another script.
  * Calling [ScriptableSingleton.Save](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableSingleton_1.Save.html).
  * Camera rendering operations. A safe alternative is to add a listener to [EditorApplication.update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html) and perform the rendering during the next Editor Update call.


* * *
