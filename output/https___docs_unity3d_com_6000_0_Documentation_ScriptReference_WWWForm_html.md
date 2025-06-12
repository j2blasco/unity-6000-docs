* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WWWForm.html

# WWWForm
class in UnityEngine
/
Implemented in:[UnityEngine.UnityWebRequestModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UnityWebRequestModule.html)
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
### Description
Helper class to generate form data to post to web servers using the [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) or WWW classes.
```
using UnityEngine;
using UnityEngine.Networking;
using System.Collections;  
  
public class WWWFormImage : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{  
  
    public string screenShotURL= "https://www.my-server.com/cgi-bin/screenshot.pl";  
  
    // Use this for initialization
    void Start()
    {
        StartCoroutine(UploadPNG());
    }  
  
    IEnumerator UploadPNG()
    {
        // We should only read the screen after all rendering is complete
        yield return new WaitForEndOfFrame[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForEndOfFrame.html)();  
  
        // Create a texture the size of the screen, RGB24 format
        int width = Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html);
        int height = Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html);
        var tex = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)( width, height, TextureFormat.RGB24[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.RGB24.html), false );  
  
        // Read screen contents into the texture
        tex.ReadPixels( new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, width, height), 0, 0 );
        tex.Apply();  
  
        // Encode texture into PNG
        byte[] bytes = tex.EncodeToPNG();
        Destroy( tex );  
  
        // Create a Web Form
        WWWForm[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WWWForm.html) form = new WWWForm[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WWWForm.html)();
        form.AddField("frameCount", Time.frameCount.ToString());
        form.AddBinaryData("fileUpload", bytes, "screenShot.png", "image/png");  
  
        // Upload to a cgi script
        using (var w = UnityWebRequest.Post[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Post.html)(screenShotURL, form))
        {
            yield return w.SendWebRequest();
            if (w.result != UnityWebRequest.Result.Success[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.Success.html)) {
                print(w.error);
            }
            else {
                print("Finished Uploading Screenshot");
            }
        }
    }
}

```

Here is a sample script that retrieves the high scores stored in a table in an SQL database.
```
using UnityEngine;
using UnityEngine.Networking;
using System.Collections;  
  
public class WWWFormScore : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    string highscore_url = "https://www.my-site.com/highscores.pl";
    string playName = "Player 1";
    int score = -1;  
  
    // Use this for initialization
    IEnumerator Start()
    {
        // Create a form object for sending high score data to the server
        WWWForm[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WWWForm.html) form = new WWWForm[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WWWForm.html)();  
  
        // Assuming the perl script manages high scores for different games
        form.AddField( "game", "MyGameName" );  
  
        // The name of the player submitting the scores
        form.AddField( "playerName", playName );  
  
        // The score
        form.AddField( "score", score );  
  
        // Create a download object
        var download = UnityWebRequest.Post[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Post.html)(highscore_url, form);  
  
        // Wait until the download is done
        yield return download.SendWebRequest();  
  
        if (download.result != UnityWebRequest.Result.Success[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.Success.html))
        {
            print( "Error[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Error.html) downloading: " + download.error );
        }
        else
        {
            // show the highscores
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(download.downloadHandler.text);
        }
    }
}

```

Here is a sample Perl script that processes the high scores stored in a table in an SQL database.
```
#!/usr/bin/perl
# The SQL database needs to have a table called highscores
# that looks something like this:
#
#   CREATE TABLE highscores (
#     game varchar(255) NOT NULL,
#     player varchar(255) NOT NULL,
#     score integer NOT NULL
#   );
#
use strict;
use CGI;
use DBI;  
  
# Read form data etc.
my $cgi = new CGI;  
  
# The results from the high score script will be in plain text
print $cgi->header("text/plain");  
  
my $game = $cgi->param('game');
my $playerName = $cgi->param('playerName');
my $score = $cgi->param('score');  
  
exit 0 unless $game; # This parameter is required  
  
# Connect to a database
my $dbh = DBI->connect( 'DBI:mysql:databasename', 'username', 'password' )
    || die "Could not connect to database: $DBI::errstr";  
  
# Insert the player score if there are any
if( $playerName && $score) {
    $dbh->do( "insert into highscores (game, player, score) values(?,?,?)",
        undef, $game, $playerName, $score );
}  
  
# Fetch the high scores
my $sth = $dbh->prepare(
    'SELECT player, score FROM highscores WHERE game=? ORDER BY score desc LIMIT 10' );
$sth->execute($game);
while (my $r = $sth->fetchrow_arrayref) {
    print join(':',@$r),"\n"
}
```

### Properties
Property | Description  
---|---  
[data](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WWWForm-data.html) | (Read Only) The raw data to pass as the POST request body when sending the form.  
[headers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WWWForm-headers.html) | (Read Only) Returns the correct request headers for posting the form using the WWW class.  
### Constructors
Constructor | Description  
---|---  
[WWWForm](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WWWForm-ctor.html) | Creates an empty WWWForm object.  
### Public Methods
Method | Description  
---|---  
[AddBinaryData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WWWForm.AddBinaryData.html) | Add binary data to the form.  
[AddField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WWWForm.AddField.html) | Add a simple field to the form.  
* * *
