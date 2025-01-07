import requests

def search_anime_scene(file_path):
    api_url = "https://api.trace.moe/search"  # API接口地址

    try:
        # 打开文件并作为POST请求发送
        with open(file_path, 'rb') as image_file:
            files = {'image': image_file}
            response = requests.post(api_url, files=files)

        # 检查请求是否成功
        response.raise_for_status()

        # 解析JSON响应
        data = response.json()

        if data.get('result'):
            result = data['result'][0]  # 获取最相关的结果
            anilist_id = result.get('anilist', 'N/A')  # anilist 是整数ID
            episode = result.get('episode', 'N/A')  # 集数
            similarity = result.get('similarity', 0) * 100  # 相似度百分比
            timestamp = result.get('from', 0)  # 时间戳
            video_preview = result.get('video', 'N/A')  # 视频预览URL
            image_preview = result.get('image', 'N/A')  # 图片预览URL

            print(f"AniList ID: {anilist_id}")
            print(f"Episode: {episode}")
            print(f"Similarity: {similarity:.2f}%")
            print(f"Timestamp: {timestamp:.2f}s")
            print(f"Video Preview: {video_preview}")
            print(f"Image Preview: {image_preview}")
        else:
            print("未找到相关的动漫场景。")

    except requests.exceptions.RequestException as e:
        print("请求时发生错误：", e)

# 替换为本地图片文件的路径
file_path = "1000.webp"  # 示例图片文件
search_anime_scene(file_path)
