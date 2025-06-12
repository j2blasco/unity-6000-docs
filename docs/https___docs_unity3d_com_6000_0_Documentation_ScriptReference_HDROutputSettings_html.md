* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings.html

# HDROutputSettings
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Provides access to HDR display settings and information.
### Static Properties
Property | Description  
---|---  
[displays](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-displays.html) | The list of currently connected displays with possible HDR availability.  
[main](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-main.html) | The HDROutputSettings for the main display.  
### Properties
Property | Description  
---|---  
[active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-active.html) | Describes whether HDR output is currently active on the display. It is true if this is the case, and @@false@ otherwise.  
[automaticHDRTonemapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-automaticHDRTonemapping.html) | Describes whether Unity performs HDR tonemapping automatically.  
[available](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-available.html) | Describes whether HDR is currently available on your primary display and that you have HDR enabled in your Unity Project. It is true if this is the case, and false otherwise.  
[displayColorGamut](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-displayColorGamut.html) | The ColorGamut used to output to the active HDR display.  
[format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-format.html) | The RenderTextureFormat of the display buffer for the active HDR display.  
[graphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-graphicsFormat.html) | The GraphicsFormat of the display buffer for the active HDR display.  
[HDRModeChangeRequested](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings.HDRModeChangeRequested.html) | Describes whether the user has requested to change the HDR Output Mode. It is true if this is the case, and false otherwise.  
[maxFullFrameToneMapLuminance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-maxFullFrameToneMapLuminance.html) | Maximum input luminance at which gradation is preserved even when the entire screen is bright.  
[maxToneMapLuminance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-maxToneMapLuminance.html) | Maximum input luminance at which gradation is preserved when 10% of the screen is bright.  
[minToneMapLuminance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-minToneMapLuminance.html) | Minimum input luminance at which gradation is identifiable.  
[paperWhiteNits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-paperWhiteNits.html) | The base luminance of a white paper surface in nits or candela per square meter (cd/m2).  
### Public Methods
Method | Description  
---|---  
[RequestHDRModeChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings.RequestHDRModeChange.html) | Use this function to request a change in the HDR Output Mode and in the value of HDROutputSettings.active.  
* * *
