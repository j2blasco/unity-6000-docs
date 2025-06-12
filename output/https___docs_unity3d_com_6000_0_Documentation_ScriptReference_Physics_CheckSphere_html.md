* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.CheckSphere.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).CheckSphere
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
public static bool CheckSphere([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, float radius, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
position | Center of the sphere.  
radius | Radius of the sphere.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Description
Returns true if there are any colliders overlapping the sphere defined by `position` and `radius` in world coordinates.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float sphereRadius;
    AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audioSource;  
  
    void Start()
    {
        audioSource = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
    }  
  
    void WarningNoise()
    {
        // Play a noise if an object is within the sphere's radius.
        if (Physics.CheckSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.CheckSphere.html)(transform.position, sphereRadius))
        {
            audioSource.Play();
        }
    }
}

```

* * *
