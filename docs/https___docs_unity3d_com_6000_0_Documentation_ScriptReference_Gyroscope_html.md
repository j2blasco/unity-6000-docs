* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gyroscope.html

# Gyroscope
class in UnityEngine
/
Implemented in:[UnityEngine.InputLegacyModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.InputLegacyModule.html)
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
Interface into the Gyroscope.
Use this class to access the gyroscope. The example script below shows how the Gyroscope class can be used to view the orientation in space of the device.  
  
Underlying sensors used for data population:  
  
**Android** : Gravity, Linear Acceleration, Rotation Vector. [ More information](https://developer.android.com/guide/topics/sensors/sensors_motion).  
  
**iOS** : Gyroscope, Device-Motion. [ More information](https://developer.apple.com/documentation/coremotion/cmmotionmanager).
```
// Create a cube with camera vector names on the faces.
// Allow the device to show named faces as it is oriented.  
  
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Faces for 6 sides of the cube
    private GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[] quads = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[6];  
  
    // Textures for each quad, should be +X, +Y etc
    // with appropriate colors, red, green, blue, etc
    public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)[] labels;  
  
    void Start()
    {
        Input.gyro.enabled = true;
        
        // make camera solid colour and based at the origin
        GetComponent<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>().backgroundColor = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(49.0f / 255.0f, 77.0f / 255.0f, 121.0f / 255.0f);
        GetComponent<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>().transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, 0);
        GetComponent<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>().clearFlags = CameraClearFlags.SolidColor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraClearFlags.SolidColor.html);  
  
        // create the six quads forming the sides of a cube
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) quad = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Quad[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Quad.html));  
  
        quads[0] = createQuad(quad, new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1,   0,   0), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0,  90, 0), "plus x",
            new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.90f, 0.10f, 0.10f, 1), labels[0]);
        quads[1] = createQuad(quad, new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0,   1,   0), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-90,   0, 0), "plus y",
            new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.10f, 0.90f, 0.10f, 1), labels[1]);
        quads[2] = createQuad(quad, new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0,   0,   1), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0,   0, 0), "plus z",
            new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.10f, 0.10f, 0.90f, 1), labels[2]);
        quads[3] = createQuad(quad, new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-1,   0,   0), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, -90, 0), "neg x",
            new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.90f, 0.50f, 0.50f, 1), labels[3]);
        quads[4] = createQuad(quad, new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0,  -1,  0), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(90,   0,  0), "neg y",
            new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.50f, 0.90f, 0.50f, 1), labels[4]);
        quads[5] = createQuad(quad, new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0,   0, -1), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 180,  0), "neg z",
            new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.50f, 0.50f, 0.90f, 1), labels[5]);  
  
        GameObject.Destroy(quad);
    }  
  
    // make a quad for one side of the cube
    GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) createQuad(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) quad, Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pos, Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) rot, string name, Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) col, Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) t)
    {
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) quat = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(rot);
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) GO = Instantiate(quad, pos, quat);
        GO.name = name;
        GO.GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>().material.color = col;
        GO.GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>().material.mainTexture = t;
        GO.transform.localScale += new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.25f, 0.25f, 0.25f);
        return GO;
    }  
  
    protected void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        GyroModifyCamera();
    }  
  
    protected void OnGUI()
    {
        GUI.skin.label.fontSize = Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 40;  
  
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Orientation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.Orientation.html): " + Screen.orientation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-orientation.html));
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("input.gyro.attitude: " + Input.gyro.attitude);
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("iphone width/font: " + Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) + " : " + GUI.skin.label.fontSize);
    }  
  
    /********************************************/  
  
    // The Gyroscope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gyroscope.html) is right-handed.  Unity is left handed.
    // Make the necessary change to the camera.
    void GyroModifyCamera()
    {
        transform.rotation = GyroToUnity(Input.gyro.attitude);
    }  
  
    private static Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) GyroToUnity(Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) q)
    {
        return new Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html)(q.x, q.y, -q.z, -q.w);
    }
}

```

![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/iOSgyroscope.png)   
_iOS Screen-shot showing +Z, +Y and -X._
### Properties
Property | Description  
---|---  
[attitude](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gyroscope-attitude.html) | Returns the attitude (ie, orientation in space) of the device.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gyroscope-enabled.html) | Sets or retrieves the enabled status of this gyroscope.  
[gravity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gyroscope-gravity.html) | Returns the gravity acceleration vector expressed in the device's reference frame.  
[rotationRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gyroscope-rotationRate.html) | Returns rotation rate as measured by the device's gyroscope.  
[rotationRateUnbiased](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gyroscope-rotationRateUnbiased.html) | Returns unbiased rotation rate as measured by the device's gyroscope.  
[updateInterval](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gyroscope-updateInterval.html) | Sets or retrieves gyroscope interval in seconds.  
[userAcceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gyroscope-userAcceleration.html) | Returns the acceleration that the user is giving to the device.  
* * *
