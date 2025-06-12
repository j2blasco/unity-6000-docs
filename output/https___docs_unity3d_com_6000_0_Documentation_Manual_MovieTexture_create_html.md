* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/MovieTexture-create.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Playing video in Movie Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/MovieTexture-landing.html)
  * Create a Movie Texture


[](https://docs.unity3d.com/6000.0/Documentation/Manual/MovieTexture-landing.html)
Playing video in Movie Textures
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MovieTexture-mobile.html)
Play video on mobile platforms
# Create a Movie Texture
To create a Movie Texture, place a video file in your project’s **Assets Folder**. Unity uses this video file in the same way as a regular [Texture](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture).
Unity imports video files using Apple QuickTime. On Windows, you need to install Quicktime to import a video file. Download Quicktime from [Apple Support Downloads](https://support.apple.com/downloads/quicktime). Unity supports the same file types as your QuickTime installation (usually **.mov** , **.mpg** , **.mpeg** , **.mp4** , **.avi** , **.asf**).
When you add a video file to your Project, Unity automatically imports it and converts it to **Ogg Theora** format. Once Unity has imported your Movie Texture, you can attach it to any **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) or **Material** An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material) in the same way as a regular Texture.
## Playing the Movie
Your Movie Texture will not play automatically when the game begins running. You must use a short script to tell it when to play.
```
// this line of code will make the Movie Texture begin playing
((MovieTexture)GetComponent<Renderer>().material.mainTexture).Play();

```

Attach the following script to toggle Movie playback when the space bar is pressed:
```
public class PlayMovieOnSpace : MonoBehaviour {
    void Update () {
        if (Input.GetButtonDown ("Jump")) {
            
            Renderer r = GetComponent<Renderer>();
            MovieTexture movie = (MovieTexture)r.material.mainTexture;
            
            if (movie.isPlaying) {
                movie.Pause();
            }
            else {
                movie.Play();
            }
        }
    }
}

```

For more information about playing Movie Textures, see the [Movie Texture Script Reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MovieTexture.html) page
### Movie Audio
When you import a Movie Texture, Unity also imports the accompanying audio track. This audio appears as an **AudioClip** child of the Movie Texture.
![The videos audio track appears as a child of the Movie Texture in the Project View](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/MovieTextureAudio.png) The video’s audio track appears as a child of the Movie Texture in the Project View
To play this audio, the **Audio Clip** A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioClip) must be attached to a GameObject. Drag the Audio Clip from the Project View onto any GameObject in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) or Hierarchy View. Usually, this will be the same GameObject that is showing the Movie. Then use [AudioSource.Play()](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Play.html) to make the the movie’s audio track play along with its video.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MovieTexture-landing.html)
Playing video in Movie Textures
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MovieTexture-mobile.html)
Play video on mobile platforms
