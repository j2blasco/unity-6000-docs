* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.SignedAngle.html

#  [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html).SignedAngle
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
public static float SignedAngle([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) from, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) to); 
### Parameters
Parameter | Description  
---|---  
from | The vector from which the angular difference is measured.  
to | The vector to which the angular difference is measured.  
### Returns
**float** The signed angle in degrees between the two vectors. 
### Description
Gets the signed angle in degrees between `from` and `to`.
The angle returned is the signed counterclockwise angle between the two vectors.  
Note: The angle returned will always be between -180 and 180 degrees, because the method returns the smallest angle between the vectors. That is, it will never return a reflex angle. Angles are calculated from world origin point (0,0,0) as the vertex.  
Additional resources: [Angle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.Angle.html) function.
```
using UnityEngine;  
  
public class Vector : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Use these to get the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s positions
    Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) m_MyFirstVector;
    Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) m_MySecondVector;  
  
    float m_Angle;  
  
    //You must assign to these two GameObjects in the Inspector
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) m_MyObject;
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) m_MyOtherObject;  
  
    void Start()
    {
        //Initialise the Vector
        m_MyFirstVector = Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);
        m_MySecondVector = Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);
        m_Angle = 0.0f;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Fetch the first GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s position
        m_MyFirstVector = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(m_MyObject.transform.position.x, m_MyObject.transform.position.y);
        //Fetch the second GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s position
        m_MySecondVector = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(m_MyOtherObject.transform.position.x, m_MyOtherObject.transform.position.y);
        //Find the angle for the two Vectors
        m_Angle = Vector2.SignedAngle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.SignedAngle.html)(m_MyFirstVector, m_MySecondVector);  
  
        //Draw lines from origin point to Vectors
        Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html), m_MyFirstVector, Color.magenta[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-magenta.html));
        Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html), m_MySecondVector, Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html));  
  
        //Log values of Vectors and angle in Console
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("MyFirstVector: " + m_MyFirstVector);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("MySecondVector: " + m_MySecondVector);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Angle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Angle.html) Between Objects: " + m_Angle);
    }  
  
    void OnGUI()
    {
        //Output the angle found above
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 25, 200, 40), "Angle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Angle.html) Between Objects" + m_Angle);
    }
}

```

* * *
