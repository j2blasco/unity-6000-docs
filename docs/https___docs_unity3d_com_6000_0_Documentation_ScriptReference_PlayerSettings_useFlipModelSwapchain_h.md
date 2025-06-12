* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-useFlipModelSwapchain.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).useFlipModelSwapchain
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
useFlipModelSwapchain; 
### Description
Use DXGI flip model swap chain for D3D11.
Direct3D 11 supports two presentation modes: Windows 7-style BitBlt and the modern flip models. The BitBlt model has historically been the only way to present the Direct3D swap chain to the screen. Every time a frame needs to be displayed, it makes a copy of the swap chain surface and blits it to the screen buffer. Windows 8.1 introduced the DXGI flip model, enabling the Desktop Window Manager to use the swap chain surface directly.  
  
DXGI flip model swap chain ensures the best performance. When running in windowed mode, it increases the performance by eliminating the expensive and redundant surface blit to the screen buffer. When running in windowed (borderless) full-screen mode, it displays the application swap chain directly on the screen, which reduces input latency by one frame and eliminates desktop composition done by the Desktop Window Manager in the same way that exclusive full-screen does. This optimization is known as "Independent Flip."  
  
To take advantage of the DXGI flip model with Direct3D 11, you need to run the player on Windows 8.1 or higher and not use [FullScreenMode.ExclusiveFullScreen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FullScreenMode.ExclusiveFullScreen.html). If either of these conditions is unmet, Unity will fall back to using Windows 7-style BitBlt swap chain model automatically, even if this setting is enabled. Unity uses the BitBlt model when using exclusive full-screen mode as flip model swap chains don't support frame latency waitable objects when running in exclusive full-screen mode, which makes them have increased input latency.  
  
DXGI flip model swap chains don't support transparency when using the [DwmExtendFrameIntoClientArea](https://docs.microsoft.com/en-us/windows/win32/api/dwmapi/nf-dwmapi-dwmextendframeintoclientarea) function, so if you need to make parts of your window transparent or invisible, you will have to disable this setting and use BitBlt model swap chain.  
  
Unity defaults to using the DXGI flip model for the Direct3D 11 graphics API. Unity always uses the DXGI flip model when using Direct3D 12, so this setting solely affects Direct3D 11. It's best practice to keep this setting enabled.  
  
Flip model swap chain can be forced in the built player by passing it the "-force-d3d11-flip-model" command-line argument. Likewise, the BitBlt model swap chain can be forced by passing the "-force-d3d11-bitblt-model" command-line argument.  
  
See <https://docs.microsoft.com/en-us/windows/win32/direct3ddxgi/dxgi-flip-model> and <https://docs.microsoft.com/en-us/windows/win32/direct3ddxgi/for-best-performance--use-dxgi-flip-model> for more information.
* * *
