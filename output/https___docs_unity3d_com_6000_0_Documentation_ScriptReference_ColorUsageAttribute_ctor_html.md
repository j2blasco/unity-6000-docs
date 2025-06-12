* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorUsageAttribute-ctor.html

# ColorUsageAttribute Constructor
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
public ColorUsageAttribute(bool showAlpha); 
## Declaration
public ColorUsageAttribute(bool showAlpha, bool hdr); 
**Obsolete** Brightness and exposure parameters are no longer used for anything. Use ColorUsageAttribute(bool showAlpha, bool hdr).
## Declaration
public ColorUsageAttribute(bool showAlpha, bool hdr, float minBrightness, float maxBrightness, float minExposureValue, float maxExposureValue); 
### Parameters
Parameter | Description  
---|---  
showAlpha | If false then the alpha channel info is hidden both in the ColorField and in the Color Picker.  
hdr | Set to true if the color should be treated as a HDR color (default value: false).  
minBrightness | Minimum allowed HDR color component value when using the HDR Color Picker (default value: 0).  
maxBrightness | Maximum allowed HDR color component value when using the HDR Color Picker (default value: 8).  
minExposureValue | Minimum exposure value allowed in the HDR Color Picker (default value: 1/8 = 0.125).  
maxExposureValue | Maximum exposure value allowed in the HDR Color Picker (default value: 3).  
### Description
Attribute for Color fields. Used for configuring the GUI for the color.
* * *
