* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetUVDistributionMetric.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).GetUVDistributionMetric
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html "Go to Mesh Component in the Manual")
## Declaration
public float GetUVDistributionMetric(int uvSetIndex); 
### Parameters
Parameter | Description  
---|---  
uvSetIndex | UV set index to return the UV distibution metric for. 0 for first.  
### Returns
**float** Average of triangle area / uv area. 
### Description
The UV distribution metric can be used to calculate the desired mipmap level based on the position of the camera.
The example code shows how this value can be used with some camera properties to calculate a required mipmap level.
```
using UnityEngine;  
  
public class MyMipmapClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_CameraPosition;
    private float m_CameraEyeToScreenDistanceSquared;  
  
    private float m_MeshUVDistributionMetric;
    private float m_TexelCount;
    private Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) m_Texture;  
  
    public void SetView(Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) cameraPosition, float cameraHalfAngle, float screenHalfHeight, float aspectRatio)
    {
        m_CameraPosition = cameraPosition;
        m_CameraEyeToScreenDistanceSquared = Mathf.Pow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Pow.html)(screenHalfHeight / Mathf.Tan[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Tan.html)(cameraHalfAngle), 2.0f);  
  
        // Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) to using the horizontal dimension if larger
        if (aspectRatio > 1.0f)    // Width is larger than height
            m_CameraEyeToScreenDistanceSquared *= aspectRatio;
    }  
  
    public void SetView(Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera)
    {
        float cameraHA = Mathf.Deg2Rad[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Deg2Rad.html) * camera.fieldOfView * 0.5f;
        float screenHH = (float)camera.pixelHeight * 0.5f;
        SetView(camera.transform.position, cameraHA, screenHH, camera.aspect);
    }  
  
    private int CalculateMipmapLevel(Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds, float uvDistributionMetric, float texelCount)
    {
        // based on  http://web.cse.ohio-state.edu/~crawfis.3/cse781/Readings/MipMapLevels-Blog.html
        // screenArea = worldArea * (ScreenPixels/(D*tan(FOV)))^2
        // mip = 0.5 * log2 (uvArea / screenArea)
        float dSq = bounds.SqrDistance(m_CameraPosition);
        if (dSq < 1e-06)
            return 0;  
  
        // uvDistributionMetric is the average of triangle area / uv area (a ratio from world space triangle area to normalised uv area)
        // - triangle area is in world space
        // - uv area is in normalised units (0->1 rather than 0->texture size)  
  
        // m_CameraEyeToScreenDistanceSquared / dSq is the ratio of screen area to world space area  
  
        float v = (texelCount * dSq) / (uvDistributionMetric * m_CameraEyeToScreenDistanceSquared);
        float desiredMipLevel = 0.5f * Mathf.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Log.html)(v, 2);  
  
        return (int)desiredMipLevel;
    }  
  
    // Pick the larger two scales of the 3 components and multiply together
    float GetLargestAreaScale(float x, float y, float z)
    {
        if (x > y)
        {
            if (y > z)
                return x * y;
            else
                return x * z;
        }
        else // x <= y
        {
            if (x < z)
                return y * z;
            else
                return x * y;
        }
    }  
  
    public void Start()
    {
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().sharedMesh;
        m_MeshUVDistributionMetric = mesh.GetUVDistributionMetric(0);  
  
        // If the mesh has a transform scale or uvscale it would need to be applied here  
  
        // Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) scale:
        // Use two scale values as we need an 'area' scale.
        // Use the two largest component to usa a more conservative selection and pick the higher resolution mip
        m_MeshUVDistributionMetric *= GetLargestAreaScale(transform.lossyScale.x, transform.lossyScale.y, transform.lossyScale.z);  
  
        // To determine uv scale for a material use Material.GetTextureScale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetTextureScale.html)
        // If there is a uv scale to apply then divide the m_MeshUVDistributionMetric by (uvScale.x * uvScale.y)  
  
        m_TexelCount = m_Texture.width * m_Texture.height;
    }  
  
    public void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        SetView(Camera.main[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html));  
  
        m_Texture.requestedMipmapLevel = CalculateMipmapLevel(GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>().bounds, m_MeshUVDistributionMetric, m_TexelCount);
    }
}

```

* * *
