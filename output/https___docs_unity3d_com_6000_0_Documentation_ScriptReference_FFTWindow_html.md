* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FFTWindow.html

# FFTWindow
enumeration
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
Spectrum analysis windowing types.
Use this to reduce leakage of signals across frequency bands.
### Properties
Property | Description  
---|---  
[Rectangular](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FFTWindow.Rectangular.html) | W[n] = 1.0.  
[Triangle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FFTWindow.Triangle.html) | W[n] = 1 - abs(2n/N - 1).  
[Hamming](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FFTWindow.Hamming.html) | W[n] = 0.54 - 0.46 * cos(2π * n/N).  
[Hanning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FFTWindow.Hanning.html) | W[n] = 0.5 * (1.0 - cos(2π * n/N)).  
[Blackman](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FFTWindow.Blackman.html) | W[n] = 0.42 - 0.5 * cos(2π * n/N) + 0.08 * cos(4π * n/N).  
[BlackmanHarris](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FFTWindow.BlackmanHarris.html) | W[n] = 0.35875 - 0.48829 * cos(2π * n/N) + 0.14128 * cos(4π * n/N) - 0.01168 * cos(6π * n/N).  
* * *
