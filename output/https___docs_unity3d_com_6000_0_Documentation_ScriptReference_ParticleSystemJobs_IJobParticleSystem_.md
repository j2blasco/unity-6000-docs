* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemJobs.IJobParticleSystem.Execute.html

#  [IJobParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemJobs.IJobParticleSystem.html).Execute
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
public void Execute([ParticleSystemJobs.ParticleSystemJobData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemJobs.ParticleSystemJobData.html) jobData); 
### Parameters
Parameter | Description  
---|---  
jobData | Contains the particle properties.  
### Description
Implement this method to access and modify particle properties.
You can use the following script to attract particles to a supplied position.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using Unity.Collections;
using UnityEngine;
using UnityEngine.ParticleSystemJobs;  
  
public class ParticleJob : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float effectRange = 2.0f;
    public float effectStrength = 1.0f;
    public float oscillationSpeed = 12.0f;
    public bool useJobSystem = false;  
  
    private float oscillationPhase;  
  
    private ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps;
    private UpdateParticlesJob job = new UpdateParticlesJob();
    private ParticleSystem.Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html)[] mainThreadParticles;  
  
    private static float Remap(float x, float x1, float x2, float y1, float y2)
    {
        var m = (y2 - y1) / (x2 - x1);
        var c = y1 - m * x1;  
  
        return m * x + c;
    }  
  
    private static Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) CalculateVelocity(ref UpdateParticlesJob job, Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) delta)
    {
        float attraction = job.effectStrength / job.effectRangeSqr;
        return delta.normalized * attraction;
    }  
  
    private static Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) CalculateColor(ref UpdateParticlesJob job, Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) delta, Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) srcColor, UInt32 seed)
    {
        var targetColor = new Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html)((byte)(seed >> 24), (byte)(seed >> 16), (byte)(seed >> 8), srcColor.a);
        float lerpAmount = delta.magnitude * job.inverseEffectRange;
        lerpAmount = lerpAmount * 0.25f + 0.75f;
        return Color32.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.Lerp.html)(targetColor, srcColor, lerpAmount);
    }  
  
    void Start()
    {
        ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        oscillationPhase = UnityEngine.Random.Range(0.0f, Mathf.PI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PI.html) * 2.0f);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) mouse = Input.mousePosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html);
        job.effectPosition = Camera.main.ScreenToWorldPoint(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(mouse.x, mouse.y, -Camera.main.transform.position.z));
        job.effectRangeSqr = effectRange * effectRange;
        job.effectStrength = effectStrength * Remap(Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(oscillationPhase + Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) * oscillationSpeed), -1, 1, -1, 0.5f);
        job.inverseEffectRange = (1.0f / effectRange);  
  
        if (!useJobSystem)
        {
            if (mainThreadParticles == null)
                mainThreadParticles = new ParticleSystem.Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html)[ps.main.maxParticles];  
  
            var count = ps.GetParticles(mainThreadParticles);
            for (int i = 0; i < count; i++)
            {
                Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position = mainThreadParticles[i].position;
                Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) delta = position - job.effectPosition;
                if (delta.sqrMagnitude < job.effectRangeSqr)
                {
                    mainThreadParticles[i].velocity += CalculateVelocity(ref job, delta);
                    mainThreadParticles[i].startColor = CalculateColor(ref job, delta, mainThreadParticles[i].startColor, mainThreadParticles[i].randomSeed);
                }
            }
            ps.SetParticles(mainThreadParticles, count);
        }
    }  
  
    void OnParticleUpdateJobScheduled()
    {
        if (useJobSystem)
            job.Schedule(ps);
    }  
  
    struct UpdateParticlesJob : IJobParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemJobs.IJobParticleSystem.html)
    {
        [ReadOnly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.html)]
        public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) effectPosition;  
  
        [ReadOnly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.html)]
        public float effectRangeSqr;  
  
        [ReadOnly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.html)]
        public float effectStrength;  
  
        [ReadOnly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.html)]
        public float inverseEffectRange;  
  
        public void Execute(ParticleSystemJobData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemJobs.ParticleSystemJobData.html) particles)
        {
            var positionsX = particles.positions.x;
            var positionsY = particles.positions.y;
            var positionsZ = particles.positions.z;  
  
            var velocitiesX = particles.velocities.x;
            var velocitiesY = particles.velocities.y;
            var velocitiesZ = particles.velocities.z;  
  
            var colors = particles.startColors;  
  
            var randomSeeds = particles.randomSeeds;  
  
            for (int i = 0; i < particles.count; i++)
            {
                Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(positionsX[i], positionsY[i], positionsZ[i]);
                Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) delta = (position - effectPosition);
                if (delta.sqrMagnitude < effectRangeSqr)
                {
                    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) velocity = CalculateVelocity(ref this, delta);  
  
                    velocitiesX[i] += velocity.x;
                    velocitiesY[i] += velocity.y;
                    velocitiesZ[i] += velocity.z;  
  
                    colors[i] = CalculateColor(ref this, delta, colors[i], randomSeeds[i]);
                }
            }
        }
    }
}

```

You can use the following script with the above example to supply the mouse position as the point to attract particles towards.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class ParticleSpawner : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) prefab;
    public int systemCount = 128;
    public int particleEmissionRatePerSystem = 400;
    public float particleSystemShapeRadius = 1.0f;
    public float totalRadius = 5.0f;
    public float effectRange = 3.0f;
    public float effectStrength = 1.0f;
    public float oscillationSpeed = 10.0f;
    public bool hasTrails = true;
    public bool useJobSystem = false;  
  
    void Start()
    {
        var material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Legacy Shaders/Particles/Additive"));
        material.SetTexture("_MainTex", AssetDatabase.GetBuiltinExtraResource<Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)>("Default-Particle.psd"));  
  
        for (int i = 0; i < systemCount; i++)
        {
            var go = GameObject.Instantiate(prefab);
            var ps = go.GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();  
  
            go.GetComponent<ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html)>().sharedMaterial = material;  
  
            float x = (float)i / systemCount;
            float theta = x * Mathf.PI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PI.html) * 2;  
  
            var transform = go.GetComponent<Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)>();
            transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(theta), Mathf.Cos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Cos.html)(theta), 0.0f) * totalRadius;  
  
            var main = ps.main;
            main.startColor = Color.HSVToRGB[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.HSVToRGB.html)(x, Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0.5f, 1.0f), Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0.5f, 1.0f));  
  
            var emission = ps.emission;
            emission.rateOverTime = particleEmissionRatePerSystem;  
  
            var shape = ps.shape;
            shape.radius = particleSystemShapeRadius;  
  
            var trails = ps.trails;
            trails.enabled = hasTrails;  
  
            var updateJob = go.GetComponent<ParticleJob>();
            updateJob.effectRange = effectRange;
            updateJob.effectStrength = effectStrength;
            updateJob.oscillationSpeed = oscillationSpeed;
            updateJob.useJobSystem = useJobSystem;
        }
    }  
  
    // UI
    void OnGUI()
    {
        float x = 25.0f;
        float y = 60.0f;
        float spacing = 40.0f;  
  
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();  
  
        GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) backgroundStyle = new GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html)(GUI.skin.box);
        backgroundStyle.normal.background = Texture2D.whiteTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-whiteTexture.html);
        var oldColor = GUI.backgroundColor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-backgroundColor.html);
        GUI.backgroundColor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-backgroundColor.html) = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.5f, 0.5f, 0.5f, 0.5f);
        GUI.Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Box.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(x - 10, y - 35, 260, 230), "Options[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Options.html)", backgroundStyle);
        GUI.backgroundColor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-backgroundColor.html) = oldColor;  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(x, y, 140, 30), "Effect Range");
        effectRange = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(x + 140, y + 5, 100, 30), effectRange, 0.0f, 10.0f);
        y += spacing;  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(x, y, 140, 30), "Effect Strength");
        effectStrength = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(x + 140, y + 5, 100, 30), effectStrength, 0.0f, 10.0f);
        y += spacing;  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(x, y, 140, 30), "Oscillation Speed");
        oscillationSpeed = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(x + 140, y + 5, 100, 30), oscillationSpeed, 0.0f, 20.0f);
        y += spacing;  
  
        hasTrails = GUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(x, y + 5, 140, 30), hasTrails, "Trails[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Trails.html)");
        y += spacing;  
  
        useJobSystem = GUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(x, y + 5, 140, 30), useJobSystem, "Use C# Job System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html)");
        y += spacing;  
  
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            ParticleJob[] updateJobs = GameObject.FindObjectsOfType<ParticleJob>();
            for (int i = 0; i < updateJobs.Length; i++)
            {
                var updateJob = updateJobs[i];
                updateJob.effectRange = effectRange;
                updateJob.effectStrength = effectStrength;
                updateJob.oscillationSpeed = oscillationSpeed;
                updateJob.useJobSystem = useJobSystem;  
  
                var ps = updateJob.GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();  
  
                var trails = ps.trails;
                trails.enabled = hasTrails;
            }
        }
    }
}

```

* * *
