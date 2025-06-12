* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.VisionUtility.GetColorBlindSafePalette.html

#  [VisionUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.VisionUtility.html).GetColorBlindSafePalette
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
public static int GetColorBlindSafePalette(Color[] palette, float minimumLuminance, float maximumLuminance); 
### Parameters
Parameter | Description  
---|---  
palette | An array of colors to populate with a palette.  
minimumLuminance | Minimum allowable perceived luminance from 0 to 1. A value of 0.2 or greater is recommended for dark backgrounds.  
maximumLuminance | Maximum allowable perceived luminance from 0 to 1. A value of 0.8 or less is recommended for light backgrounds.  
### Returns
**int** The number of unambiguous colors in the palette. 
### Description
Gets a palette of colors that should be distinguishable for normal vision, deuteranopia, protanopia, and tritanopia.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/ColorBlindSafePaletteTable.png) _The set of colors from which to draw, along with their perceived luminance values._  
  
Allocate the size of your palette before passing it to this method to specify how many colors you need. The return value indicates how many unambiguous colors exist in the palette. If this value is less than the size of the palette, then the palette repeats colors in order.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/ColorBlindSafePalette.png) _A window to preview swatches that should be distinguishable for most vision conditions._  
  
Add the following script to Assets/Editor as ColorSwatchExample.cs and navigate to the menu option Window -> Color Swatch Example.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.Accessibility;  
  
public class ColorSwatchExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    // size of swatch background textures to generate
    private const int k_SwatchTextureSize = 16;
    // the maximum number of swatches for this example
    private const int k_MaxPaletteSize = 10;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) Swatch Example")]
    private static void CreateWindow()
    {
        var window = GetWindow<ColorSwatchExample>();
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0f, 0f, 400f, 80f);
    }  
  
    // the background textures to use for the swatches
    private Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)[] m_SwatchBackgrounds = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)[k_MaxPaletteSize];  
  
    // the desired number of swatches
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private int m_PaletteSize = 8;
    // the range of desired luminance values
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) m_DesiredLuminance = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0.2f, 0.9f);
    // the colors obtained
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[] m_Palette;
    // the number of unique colors in the palette before they repeat
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private int m_NumUniqueColors;  
  
    // create swatch background textures when window first opens
    protected virtual void OnEnable()
    {
        titleContent = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) Swatches");  
  
        // create background swatches with different patterns for repeated colors
        m_SwatchBackgrounds[0] = CreateSwatchBackground(k_SwatchTextureSize, 0, 0);
        m_SwatchBackgrounds[1] = CreateSwatchBackground(k_SwatchTextureSize, 1, 4);
        m_SwatchBackgrounds[2] = CreateSwatchBackground(k_SwatchTextureSize, 1, 3);
        m_SwatchBackgrounds[3] = CreateSwatchBackground(k_SwatchTextureSize, 6, 1);
        m_SwatchBackgrounds[4] = CreateSwatchBackground(k_SwatchTextureSize, 4, 3);
        m_SwatchBackgrounds[5] = CreateSwatchBackground(k_SwatchTextureSize, 6, 6);
        m_SwatchBackgrounds[6] = CreateSwatchBackground(k_SwatchTextureSize, 4, 2);
        m_SwatchBackgrounds[7] = CreateSwatchBackground(k_SwatchTextureSize, 6, 4);
        m_SwatchBackgrounds[8] = CreateSwatchBackground(k_SwatchTextureSize, 2, 5);
        m_SwatchBackgrounds[9] = CreateSwatchBackground(k_SwatchTextureSize, 1, 2);  
  
        UpdatePalette();
    }  
  
    // clean up textures when window is closed
    protected virtual void OnDisable()
    {
        for (int i = 0, count = m_SwatchBackgrounds.Length; i < count; ++i)
            DestroyImmediate(m_SwatchBackgrounds[i]);
    }  
  
    protected virtual void OnGUI()
    {
        // input desired number of colors and luminance values
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();  
  
        m_PaletteSize = EditorGUILayout.IntSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntSlider.html)("Palette Size", m_PaletteSize, 0, k_MaxPaletteSize);  
  
        float min = m_DesiredLuminance.x;
        float max = m_DesiredLuminance.y;
        EditorGUILayout.MinMaxSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.MinMaxSlider.html)("Luminance Range", ref min, ref max, 0f, 1f);
        m_DesiredLuminance = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(min, max);  
  
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            UpdatePalette();
        }  
  
        // display warning message if parameters are out of range
        if (m_NumUniqueColors == 0)
        {
            string warningMessage = "Unable to generate any unique colors with the specified luminance requirements.";
            EditorGUILayout.HelpBox[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.HelpBox.html)(warningMessage, MessageType.Warning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MessageType.Warning.html));
        }
        // otherwise display swatches in a row
        else
        {
            using (new GUILayout.HorizontalScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.HorizontalScope.html)())
            {
                GUILayout.FlexibleSpace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.FlexibleSpace.html)();
                Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) oldColor = GUI.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html);  
  
                int swatchBackgroundIndex = 0;
                for (int i = 0; i < m_PaletteSize; ++i)
                {
                    // change swatch background pattern when reaching a repeated color
                    if (i > 0 && i % m_NumUniqueColors == 0)
                        ++swatchBackgroundIndex;  
  
                    Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect = GUILayoutUtility.GetRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayoutUtility.GetRect.html)(k_SwatchTextureSize * 2, k_SwatchTextureSize * 2);
                    rect.width = k_SwatchTextureSize * 2;  
  
                    GUI.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html) = m_Palette[i];
                    GUI.DrawTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DrawTexture.html)(rect, m_SwatchBackgrounds[swatchBackgroundIndex], ScaleMode.ScaleToFit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScaleMode.ScaleToFit.html), true);
                }  
  
                GUI.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html) = oldColor;
                GUILayout.FlexibleSpace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.FlexibleSpace.html)();
            }
        }
    }  
  
    // create a white texture with some pixels discarded to make a pattern
    private Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) CreateSwatchBackground(int size, int discardPixelCount, int discardPixelStep)
    {
        var swatchBackground = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(size, size);
        swatchBackground.hideFlags = HideFlags.HideAndDontSave[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideAndDontSave.html);
        swatchBackground.filterMode = FilterMode.Point[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.Point.html);  
  
        var pixels = swatchBackground.GetPixels32();
        int counter = 0;
        bool discard = false;
        for (int i = 0, count = pixels.Length; i < count; ++i)
        {
            pixels[i] = new Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html)(255, 255, 255, (byte)(discard ? 0 : 255));
            ++counter;
            if (discard && counter == discardPixelCount)
            {
                discard = false;
                counter = 0;
            }
            else if (!discard && counter == discardPixelStep)
            {
                discard = true;
                counter = 0;
            }
        }
        swatchBackground.SetPixels32(pixels);  
  
        swatchBackground.Apply();
        return swatchBackground;
    }  
  
    // request new palette
    private void UpdatePalette()
    {
        m_Palette = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[m_PaletteSize];
        m_NumUniqueColors =
            VisionUtility.GetColorBlindSafePalette[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.VisionUtility.GetColorBlindSafePalette.html)(m_Palette, m_DesiredLuminance.x, m_DesiredLuminance.y);
    }
}

```

* * *
