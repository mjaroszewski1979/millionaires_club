import fastapi
from fastapi.templating import Jinja2Templates
from fastapi import Request, Form, Depends, HTTPException, status
from starlette.requests import Request
from cpi import data, get_cpi_all, get_cpi_g5


templates = Jinja2Templates('templates')


router = fastapi.APIRouter()

cpi = get_cpi_g5()

@router.get("/")
def form_get(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})

@router.post("/")
def form_post(request: Request, country: str = Form(...)):
    result = str(country).upper()
    if result in data:
        try:
            ticker = data[result]
            cpi = get_cpi_all(ticker)
            return templates.TemplateResponse('index.html', context={'request': request, 'cpi': cpi, 'result': result})
        except ConnectionError:
            msg = 'Sorry, there was a problem with your request. Please try again later'
            return templates.TemplateResponse('index.html', context={'request': request, 'msg': msg})
    else:
        msg = 'PLEASE TRY A DIFFERENT COUNTRY!'
        return templates.TemplateResponse('index.html', context={'request': request, 'msg': msg})

@router.get("/about")
def about(request: Request):
    return templates.TemplateResponse("about.html", {'request': request})

@router.get("/countries")
def countries(request: Request):
    return templates.TemplateResponse("countries.html", {'request': request})

@router.get("/g5")
def g5_get(request: Request):
    nums = range(5)
    msg = 'Connection error. Please try again.'
    try:
        return templates.TemplateResponse('g5.html', context={'request': request, 'cpi': cpi, 'nums': nums})
    except:
        len(cpi) < 5
        return templates.TemplateResponse("countries.html", {'request': request, 'msg': msg})
        


    
