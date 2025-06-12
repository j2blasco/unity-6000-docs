* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WSA-transparentSwapchain.html

#  [PlayerSettings.WSA](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WSA.html).transparentSwapchain
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
transparentSwapchain; 
### Description
Sets AlphaMode on the swap chain to DXGI_ALPHA_MODE_PREMULTIPLIED.
This setting is only used for UWP projects that use the XAML build type. By enabling this setting, you will be able to compose Unity content with other XAML content in your application. Note that because the swapchain assumes premultiplied alpha, you may need to make adjustments to your content to achieve the expected output, particularly for transparent content.
* * *
