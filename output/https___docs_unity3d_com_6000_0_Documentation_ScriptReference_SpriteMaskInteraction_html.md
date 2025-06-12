* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.html

# SpriteMaskInteraction
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
This enum controls the mode under which the sprite will interact with the masking system.
Sprites by default do not interact with masks [SpriteMaskInteraction.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.None.html). A sprite can also be setup to be visible in presence of one or more masks [SpriteMaskInteraction.VisibleInsideMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.VisibleInsideMask.html) or to be visible on areas where no masks are present [SpriteMaskInteraction.VisibleOutsideMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.VisibleOutsideMask.html).
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.None.html) | The sprite will not interact with the masking system.  
[VisibleInsideMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.VisibleInsideMask.html) | The sprite will be visible only in areas where a mask is present.  
[VisibleOutsideMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.VisibleOutsideMask.html) | The sprite will be visible only in areas where no mask is present.  
* * *
