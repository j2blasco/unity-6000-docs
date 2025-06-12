* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.SetScheduledEndTime.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).SetScheduledEndTime
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html "Go to AudioSource Component in the Manual")
## Declaration
public void SetScheduledEndTime(double time); 
### Parameters
Parameter | Description  
---|---  
time | Time in seconds.  
### Description
Changes the time at which a sound that has already been scheduled to play will end. Notice that depending on the timing not all rescheduling requests can be fulfilled.
Note that the time specified is still a time on the absolute time-line, meaning that the sound will stop when reaching that time, regardless of when it was started. So if you have a 5 second long sound and want it to play at time T and stop after 3 seconds (i.e. silencing the last 2 seconds of the sound), you need to specify the end time to be T+3. This function is useful in music systems to overcome the discontinuities in signals that frame-based lossy codecs cause.
```
using UnityEngine;
using System.Collections;  
  
// While this may seem unnecessarily complicated to do this in the case of uncompressed sounds, you can now use
// the SavWav code from https://gist.github.com/2317063 to save the generated clips into new assets,
// run the program once with a specified sourceClip and the script will generate "cut1.wav" and "cut2.wav".
// These can now be imported into Unity as assets and changed to compressed sounds.
// Since psychoacoustic compression severely alters the waveforms and frequency content of sounds and
// furthermore operates in a block-based fashion, it would cause very noticeable pops and clicks if we didn't
// have the sound data after and before the cut point. By having it, even though we are not playing it, the decoder is "warmed up",
// i.e. it has matching frequency content before and after the transition, so at least the
// frequency spectrum will be more or less the same before and after the transition and so the click will be less audible
// than if we had just cut up the sound without the 0.2s overlap regions.
// This method may also be combined with cross-fading in order to further smoothen out any remaining artifacts.
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) sourceClip;
    private AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audio1;
    private AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) audio2;
    private AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) cutClip1;
    private AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) cutClip2;
    private float overlap = 0.2F;
    private int len1 = 0;
    private int len2 = 0;
    void Start()
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) child;
        child = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Player1");
        child.transform.parent = gameObject.transform;
        audio1 = child.AddComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
        child = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Player2");
        child.transform.parent = gameObject.transform;
        audio2 = child.AddComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
        int overlapSamples;
        if (sourceClip != null)
        {
            len1 = sourceClip.samples / 2;
            len2 = sourceClip.samples - len1;
            overlapSamples = (int)(overlap * sourceClip.frequency);
            cutClip1 = AudioClip.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.Create.html)("cut1", len1 + overlapSamples, sourceClip.channels, sourceClip.frequency, false, false);
            cutClip2 = AudioClip.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.Create.html)("cut2", len2 + overlapSamples, sourceClip.channels, sourceClip.frequency, false, false);
            float[] smp1 = new float[(len1 + overlapSamples) * sourceClip.channels];
            float[] smp2 = new float[(len2 + overlapSamples) * sourceClip.channels];
            sourceClip.GetData(smp1, 0);
            sourceClip.GetData(smp2, len1 - overlapSamples);
            cutClip1.SetData(smp1, 0);
            cutClip2.SetData(smp2, 0);
        }
        else
        {
            overlapSamples = (int)overlap * cutClip1.frequency;
            len1 = cutClip1.samples - overlapSamples;
            len2 = cutClip2.samples - overlapSamples;
        }
    }  
  
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 50, 230, 40), "Trigger source"))
            audio1.PlayOneShot(sourceClip);  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 100, 230, 40), "Trigger cut 1"))
            audio1.PlayOneShot(cutClip1);  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 150, 230, 40), "Trigger cut 2"))
            audio1.PlayOneShot(cutClip2);  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 200, 230, 40), "Play stitched"))
        {
            audio1.clip = cutClip1;
            audio2.clip = cutClip2;
            double t0 = AudioSettings.dspTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings-dspTime.html) + 3.0F;
            double clipTime1 = len1;
            clipTime1 /= cutClip1.frequency;
            audio1.PlayScheduled(t0);
            audio1.SetScheduledEndTime(t0 + clipTime1);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("t0 = " + t0 + ", clipTime1 = " + clipTime1 + ", cutClip1.frequency = " + cutClip1.frequency);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("cutClip2.frequency = " + cutClip2.frequency + ", samplerate = " + AudioSettings.outputSampleRate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings-outputSampleRate.html));
            audio2.PlayScheduled(t0 + clipTime1);
            audio2.time = overlap;
        }
    }
}

```

**Note:** If possible create clips that overlap, and use the scheduled end time for the first, and [AudioSource.time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-time.html) for the second to trim out the overlapped part, as the example above shows.
* * *
