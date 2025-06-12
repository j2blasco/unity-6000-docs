* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-ctor.html

# Vector2 Constructor
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
public Vector2(float x, float y); 
### Description
Constructs a new vector with given x, y components.
```
//This script moves a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to a new x position using a Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html).
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//Set your x position in the Inspector  
  
using UnityEngine;  
  
public class Examples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) m_NewPosition;
    //This is the new X position. Set it in the Inspector.
    public float m_XPosition;  
  
    // Use this for initialization
    void Start()
    {
        //Initialise the vector
        m_NewPosition = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0.0f, 0.0f);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Press the space key to change the x component of the vector
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            m_NewPosition.x = m_XPosition;
        }
        //Change the position depending on the vector
        transform.position = m_NewPosition;
    }
}

```

```
//This script shows how a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) can be moved to new positions using vectors.  
  
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). Click on the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and the Inspector window appears. Change the “Second Vector” in the Inspector
//Attach a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in the MyTransform field
//Also create 3 UI Buttons (**Create**>**UI**>**Button**) and go to each of their Inspectors to change their OnClick method (click the **+** button)
//Put your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in each field. Use the **No function** dropdown to assign one Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) with the  ZeroButton method, one with PositiveButton method and the other with the GameObjectButton method.  
  

using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Use these to set the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s position
    Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) m_MyFirstVector;
    //Set this Vector in the Inspector (the position you would like the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to move to)
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) m_MySecondVector;
    Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) m_MyThirdVector;  
  
    //You must assign to this Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) in the Inspector (could be another GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html))
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) m_MyTransform;  
  
    void Start()
    {
        //Set the first vector to be at (0, 0, 0)
        m_MyFirstVector = Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);
        //Set the third vector to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you set in the Inspector's position
        m_MyThirdVector = m_MyTransform.position;
    }  
  
    public void ZeroButton()
    {
        //Press this Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) to move your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to the first vector position (0, 0)
        //Use this to move your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to the origin (be wary of parent GameObjects)
        transform.position = m_MyFirstVector;
    }  
  
    //Press this Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) to move your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to the second vector position (100, 200)
    public void PositionButton()
    {
        //Use this to move your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to a specified position
        transform.position = m_MySecondVector;
    }  
  
    //Press this Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) to move your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to the third vector position (The m_MyTransform's position)
    public void GameObjectButton()
    {
        //Use this to move your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to another GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s position
        transform.position = m_MyThirdVector;
    }
}

```

A script that converts degrees into radians. The radians are used to rotate around the origin.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
public class ExampleScene : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        float degrees = 45.0f;
        float radians = degrees * Mathf.Deg2Rad[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Deg2Rad.html);  
  
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) vec2 = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(Mathf.Cos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Cos.html)(radians), Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(radians));
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(vec2);
    }
}

```

* * *
