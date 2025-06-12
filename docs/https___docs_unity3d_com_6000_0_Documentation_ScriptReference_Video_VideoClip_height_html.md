* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-height.html

#  [VideoClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html).height
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
height; 
### Description
The height of the images in the video clip in pixels. (Read Only).
You can use this property to help get the dimensions of your video and help display your video properly. Also, you can use it to calculate the image aspect ratio.  
  
Additional resources: [VideoClip.width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-width.html), [VideoClip.length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-length.html).
```
// This script creates a plane and uses the width and height of the VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) to resize the plane. It also plays the video on the plane. 
// Assign this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html), and assign a VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) and a Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) in the Inspector.   
  
using UnityEngine;
using UnityEngine.Video;  
  
public class WidthHeightExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) videoClip;
    public Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) mainCamera;  
  
    void Start()
    {
        if (videoClip != null)
        {
            // Create a plane to project the video clip onto.
            GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) videoPlane = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Plane.html));
            // Create the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) and assign a VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html). 
            VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) videoPlayer = videoPlane.AddComponent<VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)>();
            videoPlayer.clip = videoClip;  
  
            // Set the plane to the same position as your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
            videoPlane.transform.position = transform.position;
            // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the plane to face the camera and adjust. 
            videoPlane.transform.LookAt(mainCamera.transform);
            videoPlane.transform.Rotate(90, 0, 0);  
  
            // Get the width and height of the VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) so that you can resize the plane using these. 
            float videoWidth = videoClip.width;
            float videoHeight = videoClip.height;  
  
            // Define the scaling factor to control the size of the video plane.
            float scaleFactor = 1000.0f;   
  
            // Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html) the plane to match the video's aspect ratio.
            float planeWidth = videoWidth / scaleFactor;
            float planeHeight = videoHeight / scaleFactor;
            videoPlane.transform.localScale = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(planeWidth, 1, planeHeight);  
  
            videoPlayer.Play();
        }
        else
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Please assign a video clip.");
        }
    }
}
```

* * *
