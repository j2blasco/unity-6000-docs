* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationSceneHandleUtility.ReadInts.html

#  [AnimationSceneHandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationSceneHandleUtility.html).ReadInts
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
public static void ReadInts([Animations.AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream, NativeArray<PropertySceneHandle> handles, NativeArray<int> buffer); 
### Parameters
Parameter | Description  
---|---  
stream | The animation stream.  
handles | The PropertySceneHandle array to read from.  
buffer | The buffer that stores integer values.  
### Description
Reads integer properties from the PropertySceneHandle array (handles) and stores the integers in the provided buffer. The buffer must have enough allocated space to store all values.
* * *
