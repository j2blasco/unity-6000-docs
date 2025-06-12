* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnValidate.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnValidate()
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Description
Editor-only function that Unity calls when the script is loaded or a value changes in the Inspector.
Use this to perform an action after a value changes in the Inspector; for example, making sure that data stays within a certain range.  
  
OnValidate is called at various stages during the Editor's normal operation, such as loading scenes, building a player, and entering Play Mode. See [the details of entering Play Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode-details.html).  
  
**Note:** You should not use this callback to do other tasks such as create objects or call other non-thread-safe Unity API. You should only use it to validate the data that changed. This restriction is because OnValidate can be called often when the user interacts with an inspector in the Editor, and because OnValidate can be called from threads other than Unity's main thread, such as the loading thread.  
  
**Note:** You cannot reliably perform Camera rendering operations here. Instead, you should add a listener to [EditorApplication.update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html), and perform the rendering during the next Editor Update call.
* * *
