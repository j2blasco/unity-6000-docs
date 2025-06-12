* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.PlayFullScreenMovie.html

#  [Handheld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.html).PlayFullScreenMovie
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
public static bool PlayFullScreenMovie(string path, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) bgColor = Color.black, [FullScreenMovieControlMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FullScreenMovieControlMode.html) controlMode = FullScreenMovieControlMode.Full, [FullScreenMovieScalingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FullScreenMovieScalingMode.html) scalingMode = FullScreenMovieScalingMode.AspectFit); 
### Parameters
Parameter | Description  
---|---  
path | Filesystem path to the movie file.  
bgColor | Background color.  
controlMode | How the playback controls are to be displayed.  
scalingMode | How the movie is to be scaled to fit the screen.  
### Description
Plays a full-screen movie.
The Player streams the movie directly from device storage. It's recommended to provide the movie as a separate file, not as a usual asset. Create a folder named `StreamingAssets` in the Assets folder of your Unity project to store your movie files. Unity automatically copies contents of that folder into the application bundle.  
  
Calling this function will pause Unity during movie playback. Unity resumes after the playback finishes.  
  
The first parameter `path` can be a network-based URL. The function detects it by looking for a `://` substring that follows the protocol name.  
  
**iOS:** `Handheld.PlayFullScreenMovie` internally uses `MPMoviePlayerController` object to play movies. Therefore, you should expect the same behavior and the same supported formats. `MPMoviePlayerController` supports any movie or audio files that already play correctly on an iPod or iPhone.  
  
The movie files with .mov, .mp4, .mpv, and .3gp extensions and using one of the following compression standards are supported: 
  * H.264 Baseline Profile Level 3.0 video, up to 640 x 480 at 30 fps. Note that B frames are not supported in the Baseline profile.
  * MPEG-4 Part 2 video (Simple Profile).


Calling this function initiates a transition that fades the screen from your current content to the designated background color of the Player. When playback finishes, the Player uses another fade effect to transition back to your content.  
  
For more information, refer to Apple's documentation on [MPMoviePlayerController Class Reference](http://developer.apple.com/library/ios/#DOCUMENTATION/MediaPlayer/Reference/MPMoviePlayerController_Class/Reference/Reference.html).  
  
**UWP:** On Universal Windows Platform, `Handheld.PlayFullScreenMovie` internally uses XAML MediaElement control.  
  
On Universal Windows Platform, there generally isn't a movie resolution or bitrate limit, however, higher resolution or bitrate movies consume more memory for decoding. Weaker devices also start skipping frames much sooner at extremely high resolutions. To find a list of supported formats for this platform, refer to the Microsoft documentation on [Supported audio and video formats (Windows Runtime apps)](https://learn.microsoft.com/en-us/previous-versions/windows/apps/hh986969\(v=win.10\)?redirectedfrom=MSDN).  
  
**Android:** When an Android phone is in standby mode, `Handheld.PlayFullScreenMovie` function pauses the movie playback. When the phone is turned back on, the movie playback resumes over the lock screen if you're using a developement build. You have the option to switch back to the standard lock screen display.   
  

```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Handheld.PlayFullScreenMovie[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.PlayFullScreenMovie.html)("StarWars.mp4", Color.black[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-black.html), FullScreenMovieControlMode.CancelOnInput[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FullScreenMovieControlMode.CancelOnInput.html));
    }
}

```

* * *
