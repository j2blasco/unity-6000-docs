* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.SaveToClip.html

#  [GameObjectRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.html).SaveToClip
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
public void SaveToClip([AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip); 
## Declaration
public void SaveToClip([AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip, float fps); 
## Declaration
public void SaveToClip([AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip, float fps, [Animations.CurveFilterOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.CurveFilterOptions.html) filterOptions); 
### Parameters
Parameter | Description  
---|---  
clip | The destination clip. If this clip has animation curves, they will be removed.  
fps | The frames per second (FPS) for the clip. If no value is specified, by default, this method uses 60 FPS.  
filterOptions | The filtering options for processing the animation curves when saved to the destination clip. If no options are specified, by default, this method filters out irrelevant keys by applying a light compression of 0.5 for positionError, rotationError, scaleError and floatError.  
### Description
Saves recorded animation to a destination clip.
Note: This method computes the tangents.
* * *
