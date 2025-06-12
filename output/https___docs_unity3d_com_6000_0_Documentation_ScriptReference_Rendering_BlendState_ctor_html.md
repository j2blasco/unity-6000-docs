* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendState-ctor.html

# BlendState Constructor
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
public BlendState(bool separateMRTBlend, bool alphaToMask); 
### Parameters
Parameter | Description  
---|---  
separateMRTBlend | Determines whether each render target uses a separate blend state.  
alphaToMask | Turns on alpha-to-coverage.  
### Description
Creates a new blend state with the specified values.
All blend states are initialized to [RenderTargetBlendState.defaultValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetBlendState-defaultValue.html).
* * *
