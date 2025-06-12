* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-ctor.html

# Vector3Int Constructor
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
public Vector3Int(int x, int y, int z); 
### Parameters
Parameter | Description  
---|---  
x | The X component of the Vector3Int.  
y | The Y component of the Vector3Int.  
z | The Z component of the Vector3Int.  
### Description
Initializes and returns an instance of a new Vector3Int with x, y, z components.
```
// Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
// Attach a Tilemap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.html) component to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) (Click **Add Component** button in the Inspector window and go to **2D**<**Tilemap**)
// This script sets a Tile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.html) at a Vector3Int[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.html) position
using UnityEngine;
using UnityEngine.Tilemaps;  
  
public class Vector3IntCtorExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Vector3Int[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.html) m_Position;
    Tilemap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.html) m_Tilemap;
    Tile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.html) m_Tile;  
  
    void Start()
    {
        // Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) to set the Tile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.html) at
        m_Position = new Vector3Int[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.html)(1, 5, -2);
        // Fetch the Tilemap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.html) you attach to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Tilemap = GetComponent<Tilemap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.html)>();
        // Create a Tile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.html)
        m_Tile = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<Tile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Sets a Tile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.html) at the position if a Tile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.html) does not exist at the position on the Tilemap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.html)
        if (!m_Tilemap.HasTile(m_Position))
            m_Tilemap.SetTile(m_Position, m_Tile);
    }
}

```

* * *
## Declaration
public Vector3Int(int x, int y); 
### Parameters
Parameter | Description  
---|---  
x | The X component of the Vector3Int.  
y | The Y component of the Vector3Int.  
### Description
Initializes and returns an instance of a new Vector3Int with x and y components and sets `z` to zero.
* * *
