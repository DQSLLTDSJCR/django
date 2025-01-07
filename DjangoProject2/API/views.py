import os
import requests
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
# 封装查询函数，调用 trace.moe API
def search_anime_scene(file_path):
    api_url = "https://api.trace.moe/search"  # API 的端点
    try:
        # 打开文件并发送 POST 请求
        with open(file_path, 'rb') as image_file:
            files = {'image': image_file}
            response = requests.post(api_url, files=files)
        # 确保响应成功
        response.raise_for_status()
        # 解析 JSON 响应
        data = response.json()
        # 检查是否有结果
        if data.get('result'):
            result = data['result'][0]
            anime_name = result.get('filename', '未知动漫')
            episode = result.get('episode', '未知剧集')
            similarity = result.get('similarity', 0) * 100
            timestamp = result.get('from', 0)
            video_preview = result.get('video', '')

            return {
                "anime_name": anime_name,
                "episode": episode,
                "similarity": f"{similarity:.2f}%",
                "timestamp": f"{timestamp:.2f}s",
                "video_preview": video_preview
            }
        else:
            return {"error": "未找到相关结果，请尝试上传其他图片。"}

    except requests.exceptions.RequestException as e:
        return {"error": f"请求失败：{str(e)}"}

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_file = request.FILES['image']
        file_path = default_storage.save(f"temp/{uploaded_file.name}", uploaded_file)
        temp_file_path = os.path.join(default_storage.location, file_path)
        result = search_anime_scene(temp_file_path)
        default_storage.delete(file_path)

        # 渲染结果页面
        return render(request, 'API/results.html', {"result": result})

    # 如果是 GET 请求或其他情况，渲染上传页面
    return render(request, 'API/upload.html')
