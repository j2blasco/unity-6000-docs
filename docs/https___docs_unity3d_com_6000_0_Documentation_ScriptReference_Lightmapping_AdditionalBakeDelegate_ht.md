* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.AdditionalBakeDelegate.html

#  [Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.html).AdditionalBakeDelegate
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
public delegate void AdditionalBakeDelegate(ref float progress, ref bool done); 
### Parameters
Parameter | Description  
---|---  
progress | The progress of the additional baking stage (0.0-1.0). This progress will be displayed in the progress bar.  
done | Wether the additional bake is done. Set this to true to unlock the baking pipeline.  
### Description
Delegate called at the last stage of the baking pipeline.
* * *
