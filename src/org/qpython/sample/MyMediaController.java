package org.qpython.sample;

import android.app.Activity;
import android.content.Context;
import android.view.KeyEvent;
import android.widget.MediaController;

public class MyMediaController extends MediaController {

public MyMediaController(Context context) {
    super(context);      
}

// Do nothing on the overridden hide method so the playback controls will never go away.
@Override
public void hide() {

}

// Override the dispatchKeyEvent function to capture the back KeyEvent and tell the activity to finish.
@Override
public boolean dispatchKeyEvent(KeyEvent event)
{
    if (event.getKeyCode() == KeyEvent.KEYCODE_BACK) 
    {
        ((Activity) getContext()).finish();
    }

    return super.dispatchKeyEvent(event);
}
}
