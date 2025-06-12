* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GetAllCameras.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).GetAllCameras
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
## Declaration
public static int GetAllCameras(Camera[] cameras); 
### Parameters
Parameter | Description  
---|---  
cameras | An array to be filled up with cameras currently in the Scene.  
### Description
Fills an array of Camera with the current cameras in the Scene, without allocating a new array.
The passed in array needs to be of minimum size of `allCamerasCount` . When the array size is larger than the `allCamerasCount` value, only the first elements up to allCamerasCount will be filled up. When the array size is smaller than the `allCamerasCount` value, an argument exception is thrown. When the array argument passed in is null, this call will throw a nullreference exception.  
  
The return value indicates how many cameras are saved in the array.
* * *
