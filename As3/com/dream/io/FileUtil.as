package com.dream.util
{
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	import flash.utils.ByteArray;

	/**
	 *文件工具类 
	 * @author lenovo
	 * 
	 */	
	public class FileUtil
	{
		public function FileUtil()
		{
		}
		
		/**
		 *获取文件字节数组 
		 * @param filename
		 * @return 
		 * 
		 */		
		public static function getByteArray(filename:String):ByteArray
		{
			var ba:ByteArray;
			var file:File = new File(filename);
			if(file.exists)
			{
				ba = new ByteArray();
			}
			var fs:FileStream = new FileStream();
			fs.open(file,FileMode.READ);
			fs.readBytes(ba);
			fs.close();
			return ba;
		}
	}
}