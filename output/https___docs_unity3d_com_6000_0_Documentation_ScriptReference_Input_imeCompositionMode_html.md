* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-imeCompositionMode.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).imeCompositionMode
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
[IMECompositionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMECompositionMode.html) imeCompositionMode; 
### Description
Controls enabling and disabling of IME input composition.
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
Some languages use complex input methods which involve opening windows to insert characters. Typically, this is not desirable while playing a game, as games may just interpret key strokes as game input, not as text. By default, Unity will enable IME composition when in text fields, and disable it otherwise. However, when you want to implement your own input GUI, you may want to have control over this yourself, which is possible using the imeCompositionMode property. Set it to `Auto` for the default behavior, or `On` or `Off` to explicitly enable or disable IME composition.
* * *
