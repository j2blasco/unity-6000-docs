* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-pixelAspectRatioNumerator.html

#  [VideoClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html).pixelAspectRatioNumerator
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
pixelAspectRatioNumerator; 
### Description
Returns the numerator of the pixel aspect ratio (numerator:denominator). (Read Only).
The pixel aspect ratio (for example, 10:11) determines the shape of each pixel. The first number (10) is the numerator and is the width of the pixel. The second number (11) is the denominator and is the height of the pixel. You can use the pixel aspect ratio to resize a video to appear less stretched.   
  
Additional resources: [VideoClip.pixelAspectRatioDenominator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-pixelAspectRatioDenominator.html).
```
// This script creates a plane, adds a VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component and plays a video on it. 
// It uses the pixel aspect ratio denominator and numerator to resize the plane to prevent the video appearing stretched.   
  
using UnityEngine;
using UnityEngine.Video;  
  
public class PixelAspectRatioExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) videoClip;
    public Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) mainCamera;
    void Start()
    {
        if (videoClip != null)
        {
            float numerator = (float)videoClip.pixelAspectRatioNumerator;
            float denominator = (float)videoClip.pixelAspectRatioDenominator;  
  
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
  
            // Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html) the plane to match the video's aspect ratio.
            float planeWidth = videoPlane.transform.localScale.x * numerator / denominator;
            videoPlane.transform.localScale = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(planeWidth, 1, 1);  
  
        }
        else
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("No VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) assigned in the Inspector.");
        }
    }
}
```

* * *
