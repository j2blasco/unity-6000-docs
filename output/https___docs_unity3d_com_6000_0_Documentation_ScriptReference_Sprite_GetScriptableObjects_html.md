* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.GetScriptableObjects.html

#  [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html).GetScriptableObjects
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
public uint GetScriptableObjects(ScriptableObject[] scriptableObjects); 
### Parameters
Parameter | Description  
---|---  
scriptableObjects | The array of [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) to contain the ScriptableObjects referenced by the sprite.   
### Returns
**uint** Returns the number of ScriptableObjects retrieved. 
### Description
Retrieves an array of [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) referenced by the sprite. 
If the size of the arrays passed in as parameters are less than the number of [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) referenced by the sprite, the arrays will not be resized and the results will be limited.  
  
If the size of the arrays passed in as parameters are bigger than the number of [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) referenced by the sprite, the number of elements used in the array will be indicated by the return value of the method.  
  
The following is an example usage of adding, getting and removing ScriptableObjects reference to a sprite. 
```
using UnityEngine;  
  
/*
 * Creates a custom ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) and attaches it
 * to a Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html). The ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) is then removed after
 * the first Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) loop so that the messages are only printed once.
 */  
  
// A custom ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) to hold any custom data.
public class MyScriptableObject : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public string myCustomData;
}  
  
public class Sample[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.UI.Sample.html) : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) m_Sprite;
    void Start()
    {
        var customData = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<MyScriptableObject>();
        customData.myCustomData = "My Data[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Data.html)";
        var texture = Texture2D.whiteTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-whiteTexture.html);
        m_Sprite = Sprite.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.Create.html)(texture, new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, texture.width, texture.height), Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html), texture.width);
        var spriteRenderer = gameObject.AddComponent<SpriteRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)>();
        m_Sprite.AddScriptableObject(customData);
        spriteRenderer.sprite = m_Sprite;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        var scriptableObjectCount = m_Sprite.GetScriptableObjectsCount();
        if (scriptableObjectCount > 0)
        {
            var scriptableObjects = new ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)[scriptableObjectCount];
            var retrieveCount = m_Sprite.GetScriptableObjects(scriptableObjects);
            //This will print 1 since there is 1 ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) reference.
            print(retrieveCount);
            var myScriptableObject = scriptableObjects[0] as MyScriptableObject;
            // This will print "My Data[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Data.html)"
            print(myScriptableObject.myCustomData);  
  
            // Removing the ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) reference so that the prints
            // above no longer executes.
            m_Sprite.RemoveScriptableObjectAt(scriptableObjectCount - 1);
        }
    }
}

```

* * *
