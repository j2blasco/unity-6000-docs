* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnAudioFilterRead.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnAudioFilterRead(float[], int)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Parameters
Parameter | Description  
---|---  
data | An `array of floats` comprising the audio data.  
channels | An `int` that stores the number of channels of audio data passed to this delegate.  
### Description
If OnAudioFilterRead is implemented, Unity will insert a custom filter into the audio DSP chain.
The filter is inserted in the same order as the MonoBehaviour script is shown in the Inspector.  
  
OnAudioFilterRead is called every time a chunk of audio is sent to the filter (this happens frequently, every ~20ms depending on the sample rate and platform). The audio data is an array of floats ranging from [-1.0f;1.0f] and contains audio from the previous filter in the chain or the [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) on the [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html). If this is the first filter in the chain and a clip isn't attached to the audio source, this filter will be played as the audio source. In this way you can use the filter as the audio clip, procedurally generating audio.  
  
If there is more than one channel, the channel data is interleaved. This means each consecutive data sample in the array comes from a different channel until you run out of channels and loop back to the first. `data.Length` reports the total size of the data, so to find the number of samples per channel, divide `data.Length` by `channels`.  
  
If OnAudioFilterRead is implemented a VU meter is shown in the Inspector displaying the outgoing sample level. The process time of the filter is also measured and the spent milliseconds are shown next to the VU meter. The number turns red if the filter is taking up too much time, meaning the mixer will be starved of audio data.  
  
Also note that OnAudioFilterRead is called on a different thread from the main thread (namely the audio thread) so calling into many Unity functions from this function is not allowed (if you try, a warning shows up at run time).  
  
Additional resources: [Audio Filters](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffect.html).
```
using UnityEngine;  
  
// The code example shows how to implement a metronome that procedurally
// generates the click sounds via the OnAudioFilterRead callback.
// While the game is paused or suspended, this time will not be updated and sounds
// playing will be paused. Therefore developers of music scheduling routines do not have
// to do any rescheduling after the app is unpaused  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)))]
public class AudioTest : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public double bpm = 140.0F;
    public float gain = 0.5F;
    public int signatureHi = 4;
    public int signatureLo = 4;  
  
    private double nextTick = 0.0F;
    private float amp = 0.0F;
    private float phase = 0.0F;
    private double sampleRate = 0.0F;
    private int accent;
    private bool running = false;  
  
    void Start()
    {
        accent = signatureHi;
        double startTick = AudioSettings.dspTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings-dspTime.html);
        sampleRate = AudioSettings.outputSampleRate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings-outputSampleRate.html);
        nextTick = startTick * sampleRate;
        running = true;
    }  
  
    void OnAudioFilterRead(float[] data, int channels)
    {
        if (!running)
            return;  
  
        double samplesPerTick = sampleRate * 60.0F / bpm * 4.0F / signatureLo;
        double sample = AudioSettings.dspTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings-dspTime.html) * sampleRate;
        int dataLen = data.Length / channels;  
  
        int n = 0;
        while (n < dataLen)
        {
            float x = gain * amp * Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(phase);
            int i = 0;
            while (i < channels)
            {
                data[n * channels + i] += x;
                i++;
            }
            while (sample + n >= nextTick)
            {
                nextTick += samplesPerTick;
                amp = 1.0F;
                if (++accent > signatureHi)
                {
                    accent = 1;
                    amp *= 2.0F;
                }
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Tick: " + accent + "/" + signatureHi);
            }
            phase += amp * 0.3F;
            amp *= 0.993F;
            n++;
        }
    }
}

```

* * *
