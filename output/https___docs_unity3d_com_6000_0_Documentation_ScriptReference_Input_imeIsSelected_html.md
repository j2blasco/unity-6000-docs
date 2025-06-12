* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-imeIsSelected.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).imeIsSelected
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
imeIsSelected; 
### Description
Does the user have an IME keyboard input source selected?
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
This returns true if the users keyboard is currently configured for IME input, and false otherwise. Since users of asian languages can typically turn IME conversion on or off using a keystroke, it is useful to provide some visual indication of IME being enabled. This can be done by checking [Input.imeIsSelected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-imeIsSelected.html).
* * *
