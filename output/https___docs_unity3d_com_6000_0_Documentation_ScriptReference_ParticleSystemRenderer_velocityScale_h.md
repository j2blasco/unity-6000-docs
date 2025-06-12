* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-velocityScale.html

#  [ParticleSystemRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html).velocityScale
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
velocityScale; 
### Description
Specifies how much particles stretch depending on their velocity.
Use this to make particles get longer as their speed increases.
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {  
  
    private ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps;
    private ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html) psr;
    public ParticleSystemRenderMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderMode.html) renderMode = ParticleSystemRenderMode.Billboard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderMode.Billboard.html);
    public float cameraScale = 0.0f;
    public float lengthScale = 0.0f;
    public float velocityScale = 1.0f;  
  
    void Start() {  
  
        ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        psr = GetComponent<ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html)>();  
  
        psr.mesh = Resources.GetBuiltinResource<Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)>("Capsule.fbx");  
  
        var main = ps.main;
        main.startSpeed = new ParticleSystem.MinMaxCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxCurve.html)(0.5f, 1.5f);
        main.startSize = new ParticleSystem.MinMaxCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxCurve.html)(0.1f, 0.8f);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)() {
        psr.renderMode = renderMode;
        psr.cameraVelocityScale = cameraScale;
        psr.lengthScale = lengthScale;
        psr.velocityScale = velocityScale;  
  
        if (renderMode == ParticleSystemRenderMode.Stretch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderMode.Stretch.html))
            Camera.main.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html)) * 4.0f, 0.0f, -10.0f);    // move the camera so we can see the effect on stretch camera velocity
    }  
  
    void OnGUI() {
        renderMode = (ParticleSystemRenderMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderMode.html))GUI.SelectionGrid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.SelectionGrid.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 25, 900, 30), (int)renderMode, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)[] { new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Billboard"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Stretch"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("HorizontalBillboard"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("VerticalBillboard"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("None") }, 6);  
  
        if (renderMode == ParticleSystemRenderMode.Stretch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderMode.Stretch.html)) {  
  
            GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 80, 100, 30), "Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html)");
            GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 120, 100, 30), "Length[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Length.html) Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html)");
            GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 160, 100, 30), "Velocity Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html)");  
  
            cameraScale = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(125, 85, 100, 30), cameraScale, 0.0f, 10.0f);
            lengthScale = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(125, 125, 100, 30), lengthScale, 0.0f, 10.0f);
            velocityScale = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(125, 165, 100, 30), velocityScale, 0.0f, 10.0f);
        }
    }
}

```

* * *
