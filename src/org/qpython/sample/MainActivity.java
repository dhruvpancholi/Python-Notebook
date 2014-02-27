package org.qpython.sample;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageManager;
import android.content.pm.PackageManager.NameNotFoundException;
import android.net.Uri;
import android.os.Bundle;
import android.text.method.ScrollingMovementMethod;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.view.WindowManager;
import android.webkit.WebChromeClient;
import android.webkit.WebChromeClient.CustomViewCallback;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.widget.EditText;
import android.widget.FrameLayout;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.VideoView;

/*
 * This is a sample application, which can be used for the purpose of running
 * python code on android devices with the help of QPython application
 * */

public class MainActivity extends Activity {
	static Context myContext;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		//requestWindowFeature(Window.FEATURE_NO_TITLE);
		getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
				WindowManager.LayoutParams.FLAG_FULLSCREEN);
		setContentView(R.layout.activity_main);
		// Context object saved, which can be reused for the purpose of
		// importing external content
		myContext = this;
		WebView webView = (WebView) findViewById(R.id.webView1);
		webView.setWebChromeClient(new WebChromeClient());
		webView.loadUrl("file:///android_asset/gameover.html");
		webView.getSettings().setAllowFileAccess(true); 
		WebSettings webSettings = webView.getSettings();
		webSettings.setJavaScriptEnabled(true);
		webSettings.setPluginsEnabled(true);
	    webView.setKeepScreenOn(true);
		/* VideoView videoView = (VideoView) findViewById(R.id.videoView1);

		    // Use our own media controller, which inherits from the standard one. Do this to keep 
		    // playback controls from disappearing.
		    final MyMediaController mediaController = new MyMediaController(this);
		    mediaController.setAnchorView(videoView);

		    Uri video = Uri.parse(url);

		    videoView.setMediaController(mediaController);
		    videoView.setVideoURI(video);

		    // Set a handler that will show the playback controls as soon as audio starts.
		    videoView.setOnPreparedListener(new OnPreparedListener() {

		        @Override
		        public void onPrepared(MediaPlayer arg0) {

		            mediaController.show();
		        }

		    });

		    videoView.start();
*//*		ImageView imageView = (ImageView) findViewById(R.id.imageView1);
		Bitmap bmp=null;
		URL url = null;
		try {	
			url = new URL("https://www.google.co.in/images/srpr/logo11w.png");
		
		} catch (MalformedURLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		try {
			bmp = BitmapFactory.decodeStream(url.openConnection().getInputStream());
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        imageView.setImageBitmap(bmp);*/
	}
	

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		// Extra items can be added from in the activity_main.xml
		getMenuInflater().inflate(R.menu.activity_main, menu);
		return true;
	}

	/*
	 * 
	 * 
	 */
	private final int SCRIPT_EXEC_PY = 40001;
	private final String extPlgPlusName = "com.hipipal.qpy";

	// This function checks whether the given application is installed on the
	// android device or not
	public static boolean checkAppInstalledByName(Context context,
			String packageName) {
		if (packageName == null || "".equals(packageName))
			return false;
		try {
			ApplicationInfo info = context.getPackageManager()
					.getApplicationInfo(packageName,
							PackageManager.GET_UNINSTALLED_PACKAGES);

			Log.d("QPYMAIN", "checkAppInstalledByName:" + packageName
					+ " found");
			return true;
		} catch (NameNotFoundException e) {
			Log.d("QPYMAIN", "checkAppInstalledByName:" + packageName
					+ " not found");

			return false;
		}
	}

	public void onQPyExec(View v) {

		if (checkAppInstalledByName(getApplicationContext(), extPlgPlusName)) {
			Toast.makeText(this, "Running the Python Code", Toast.LENGTH_SHORT)
					.show();

			Intent intent = new Intent();
			intent.setClassName(extPlgPlusName, extPlgPlusName + ".MPyApi");
			intent.setAction(extPlgPlusName + ".action.MPyApi");

			// Bundle is an object which is used to add string to
			// It is highly used when we need to pass the data between two
			// activities
			// or between two applications
			Bundle mBundle = new Bundle();
			mBundle.putString("app", "myappid");
			mBundle.putString("act", "onPyApi");
			mBundle.putString("flag", "onQPyExec"); // any String flag you may
													// use in your context
			mBundle.putString("param", ""); // param String param you may use in
											// your context

			// This piece of code tries to read the code from the given file
			// and also add the custom code from the user edit text
			try {
				String str = getStringFromFile("monteCarlo.py");
				EditText inputFunc = (EditText) findViewById(R.id.inputCode);
				str = str + "\n" + inputFunc.getText().toString() + "\n";
				mBundle.putString("pycode", str);
			} catch (Exception e) {
				e.printStackTrace();
			}

			intent.putExtras(mBundle);

			startActivityForResult(intent, SCRIPT_EXEC_PY);
		} else {
			Toast.makeText(getApplicationContext(),
					"Please install QPython Player first", Toast.LENGTH_LONG)
					.show();
			// Taking to the android marketplace to install the player
			// application
			try {
				Uri uLink = Uri.parse("market://details?id=com.hipipal.qpy");
				Intent intent = new Intent(Intent.ACTION_VIEW, uLink);
				startActivity(intent);
			} catch (Exception e) {
				Uri uLink = Uri.parse("http://qpython.com");
				Intent intent = new Intent(Intent.ACTION_VIEW, uLink);
				startActivity(intent);
			}

		}
	}
	public void onReset(View v) {
		EditText code = (EditText) findViewById(R.id.inputCode);
		code.setText("");
	}

	public static String convertStreamToString(InputStream is) throws Exception {
		BufferedReader reader = new BufferedReader(new InputStreamReader(is));
		StringBuilder sb = new StringBuilder();
		String line = null;
		while ((line = reader.readLine()) != null) {
			sb.append(line).append("\n");
		}
		return sb.toString();
	}

	// This function is used to return the string of the file and
	public static String getStringFromFile(String filePath) throws Exception {
		// File fl = new File(filePath);

		InputStream fin = myContext.getAssets().open(filePath);
		String ret = convertStreamToString(fin);
		// Make sure you close all streams.
		fin.close();
		return ret;
	}

	// To make the toast for the obtained result
	@Override
	protected void onActivityResult(int requestCode, int resultCode, Intent data) {
		if (requestCode == SCRIPT_EXEC_PY) {
			Bundle bundle = data.getExtras();
			String flag = bundle.getString("flag"); // flag you set
			String param = bundle.getString("param"); // param you set
			String result = bundle.getString("result"); // Result your Pycode
														// generate
			Toast.makeText(this, "" + result + "", Toast.LENGTH_SHORT).show();
			TextView code = (TextView) findViewById(R.id.textView1);
			code.setMovementMethod(new ScrollingMovementMethod());
			code.setText(""+result);
		}
	}

}
