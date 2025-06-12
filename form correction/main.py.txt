from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pose_module import analyze_pose_from_image

app = FastAPI()

# لتفعيل CORS عشان Flutter يقدر يبعت طلبات
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # يفضل تخصصها لاحقًا
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Pose Correction API is running!"}

@app.post("/analyze_pose/")
async def analyze_pose(file: UploadFile = File(...)):
    contents = await file.read()
    result = analyze_pose_from_image(contents)
    if result["success"]:
        return result
    else:
        return JSONResponse(status_code=400, content=result)
