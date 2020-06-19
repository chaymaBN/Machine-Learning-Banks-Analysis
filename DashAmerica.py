
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pickle
from pickle import load
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from app import app
import base64
import dash_table

with open ('modela.pkl','rb') as file:

    data = load(file)
with open ('data1.pkl','rb') as file:

    data1 = load(file)


image_filename = 'D:/4DS/Projet python/a.jpg' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
##################################################################################─
image_filename1 = 'D:/4DS/Projet python/pie.png' # replace with your own image
encoded_image1 = base64.b64encode(open(image_filename1, 'rb').read())
#####################################################################

image_filename2 = 'D:/4DS/Projet python/bar2.png' # replace with your own image
encoded_image2 = base64.b64encode(open(image_filename2, 'rb').read())
#####################################################################

AMa=pd.read_csv('Bank_of_America_data.csv')
AM=(AMa.dropna()).head(10)

app.layout = html.Div(className="container-fluid mb-4", children= [

    html.Div(className="jumbotron pt-4", children=[
    html.Div( className="display-6" ,children=[
     html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),height=100)] )
       ,
         html.H1(className="display-6", children="Bienvenue "),
        html.P("Projet Python  : Objectif: créer un algorithme de notation du crédit qui prédit la probabilité qu'un demandeur de prêt donné ne parvienne pas à rembourser son prêt..", className="lead"),
        html.Div(className="col-6",children=[

]),





        html.Hr(className="my-4"),html.P("", className="text-muted"),
        html.P("Cliquer sur LearnMore pour avoir plus d'informations ."),
        html.Div(className="d-flex justify-content-between ",children=[
            html.Button("Learn more",className="btn btn-primary" ),
            html.Div(className="col-6", children=[
                html.Div(className="row", children=[
                    html.Div(className="col-6 offset-4",children=[
                        dcc.Dropdown(id="bnq_selector",options=[
                        {"label":"Banque amerique", "value":"a"},
                        {"label":"Banque germany", "value":"g"},
                        {"label":"Banque taywan", "value":"t"},
                        ])
                    ]),
                    html.Button(id="go", children="voir Bank", className="btn btn-outline-success")
                ])

            ])
        ])

    ]),


    html.Div(id='intermediate-value', style={'display': 'none'}),

    html.Div(className="row", children=[
           html.Div(className="col-11 offset-1", children=[
        html.H3("Dashboard ", className="col-11 offset-1 text-dark"),
            html.Hr(className="col-10 offset-1 mb-4"), html.P("", className="text-muted"),

   html.Div(className="col-11 offset-1",children=[

   html.Img(src='data:image/png;base64,{}'.format(encoded_image1.decode()),height=400)]),
    html.Hr(className="col-10 offset-1 mb-4"), html.P("", className="text-muted"),
              html.H3("Graphe des modalités du variable JOB et leur contribution à prédire le client ", className="col-11 offset-1 text-dark mt-4"),
   html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode()),height=600)
            ]),


             ]),
             html.Div(dcc.Graph(
        id='example-graph',
        figure={

           'data': [
                {'x':AM['JOB'], 'y': AM['LOAN'], 'type': 'bar', 'name': 'LOAN'},
                {'x': AM['JOB'], 'y': AM['BAD'], 'type': 'bar', 'name': u'badd'},

            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )), html.Hr(className="col-10 offset-1 mb-4"), html.P("", className="text-muted"),

      dcc.Graph(id='device_usage',
                           figure=go.Figure(
                               data=[go.Pie(labels=['Debt consolidation', 'Home improvement'],
                                            values=[sum(data1[0]['REASON']=='DebtCon'),sum(data1[0]['REASON']=='HomeImp')      ])],
                               layout=go.Layout(
                                   title=('Raison pour avoir un prêt')
                         )  )),


 html.Hr(className="col-10 offset-1 mb-4"), html.P("", className="text-muted"),
  html.H1(className="display-6", children="Scoring d'un client d'une banque ", style={'textAlign': 'center','color': 'blue'}),


    html.Div(className="row", children=[

      html.Div(className="col-6",children=[
                html.H3( children="Formulaire à remplir :", style={'textAlign': 'center','color': 'blue'}),
                html.Hr(className="col-11 offset-1"),
                html.Div(className="p-5 ml-5 shadow",children=[
                html.Form([
                    html.Div(className="form-group col-6",children=[
                        html.Label("LOAN", htmlFor="LOAN"),
                        dcc.Input(type="number",id="LOAN", className="form-control", placeholder="enter the LOAN value"),
                        html.Small("enter the LOAN value", className="text-muted")
                    ]),


                    html.Div(className="form-group col-6",children=[
                        html.Label("REASON", htmlFor="REASON"),
                        dcc.Dropdown(id="REASON",  value="other",className="col-12 p-0", options=[
                            {'label':'DebtCon', 'value':'DebtCon'},
                            {'label':'HomeImp', 'value':'HomeImp'},

                        ]),
                        html.Small("select a REASON ", className="text-muted")
                    ]),



                    html.Div(className="form-group col-6",children=[
                        html.Label("JOB", htmlFor="JOB"),
                        dcc.Dropdown(id="JOB",  value="other",className="col-12 p-0", options=[
                            {'label':'Office', 'value':'Office'},
                            {'label':'Self', 'value':'Self'},
                            {'label':'ProfExe', 'value':'ProfExe'},
                            {'label':'others', 'value':'others'},

                        ]),
                        html.Small("select a JOB ", className="text-muted")
                    ]),


                    html.Div(className="form-group col-6",children=[
                        html.Label("MORTDUE", htmlFor="MORTDUE"),
                        dcc.Input(type="number",id="MORTDUE",  className="form-control", placeholder="enter the MORTDUE"),
                        html.Small("enter the MORTDUE", className="text-muted")
                    ]),






                    html.Div(className="form-group col-6",children=[
                        html.Label("VALUE", htmlFor="VALUE"),
                        dcc.Input(type="number",id="VALUE", min=0, max=100,  className="form-control", placeholder="Value of current property"),
                        html.Small("Value of current property", className="text-muted")
                    ]),

                    html.Div(className="form-group col-6",children=[
                        html.Label("YOJ", htmlFor="YOJ"),
                        dcc.Input(type="number",id="YOJ", min=0, max=2050,  className="form-control", placeholder="Years at present job"),
                        html.Small("Years at present job", className="text-muted")
                    ]),

                    html.Div(className="form-group col-6",children=[
                        html.Label("DEROG", htmlFor="DEROG"),
                        dcc.Input(type="number",id="DEROG", min=0, max=100000,  className="form-control", placeholder="DEROG"),
                        html.Small("DEROG", className="text-muted")
                    ]),

                    html.Div(className="form-group col-6",children=[
                        html.Label("DELINQ", htmlFor="DELINQ"),
                        dcc.Input(type="number",id="DELINQ", min=0, max=100000,  className="form-control", placeholder="DELINQ"),
                        html.Small("DELINQ", className="text-muted")
                    ]),

                    html.Div(className="form-group col-6",children=[
                        html.Label("CLAGE", htmlFor="CLAGE"),
                        dcc.Input(type="number",id="CLAGE",  min=0, max=100000, className="form-control", placeholder="CLAGE"),
                        html.Small("CLAGE", className="text-muted")
                    ]),

                    html.Div(className="form-group col-6",children=[
                        html.Label("NINQ", htmlFor="NINQ"),
                        dcc.Input(type="number",id="NINQ",  className="form-control", placeholder="amount NINQ"),
                        html.Small("NINQ", className="text-muted")
                    ]),



                    html.Div(className="form-group col-6",children=[
                        html.Label("CLNO", htmlFor="CLNO"),
                        dcc.Input(type="number",id="CLNO",  className="form-control", placeholder="CLNO"),
                        html.Small("CLNO ", className="text-muted")
                    ]),


                    html.Div(className="form-group col-6",children=[
                        html.Label("DEBTINC", htmlFor="DEBTINC"),
                        dcc.Input(type="number",id="DEBTINC",  className="form-control", placeholder="DEBTINC"),
                        html.Small("DEBTINC ", className="text-muted")
                    ]),


                    html.Div(className="form-group col-6",children=[
                        html.Label("method to test", htmlFor="method"),
                        dcc.Dropdown(id="method",  value="method",className="col-12 p-0", options=[
                            {'label':'xgboost', 'value':0},
                       {'label':'Random forest', 'value':1,'disabled': True},
                         {'label': 'KNN', 'value': 'KNN', 'disabled': True},
                         {'label': 'Random forest', 'value': 'RF', 'disabled': True},
                         {'label': 'SVM', 'value': 'SVM', 'disabled': True},
                         {'label': 'Naive Bayes', 'value': 'NB', 'disabled': True},
                         {'label': 'Logistic regression', 'value': 'RL', 'disabled': True}

                        ]),
                        html.Small("select a method ", className="text-muted")
                    ]),


                ], className="row"),
                html.Hr(),
                html.Button("Predict", className="btn btn-success", id="action_3"),
               html.Div(className="alert alert-primary text-center mt-4", children=" SVp Remplir les champs  ", id="output_msg_3"),

            ]),


   html.Hr(className="col-11 ml-5"),


        ])
    ]),html.Div([dash_table.DataTable(id='table',

style_table={
        'maxHeight': '300px',
        'overflowY': 'scroll'}


    )]), html.Div(id='body-div')
]
)

@app.callback(Output("output_msg_3","children"),[Input("action_3","n_clicks")],[
    State("LOAN","value"),
    State("REASON","value"),
    State("JOB","value"),
    State("MORTDUE","value"),
    State("VALUE","value"),
    State("YOJ","value"),
    State("DEROG","value"),
    State("DELINQ","value"),
    State("CLAGE","value"),
    State("NINQ","value"),
    State("CLNO","value"),
    State("DEBTINC","value"),
    State("method","value")

    ])



def predict_customer(inp,LOAN, REASON, JOB, MORTDUE, VALUE, YOJ, DEROG, DELINQ, CLAGE ,NINQ,CLNO,DEBTINC,method):
    if inp is not None:
         if  (REASON is None) or (MORTDUE is None) or (JOB is None)   or  (method is None):
            return  " SVp Remplir les champs  "


         if VALUE is None :
           return  " SVp Remplir les champs  "
         if YOJ is None :
            return  " SVp Remplir les champs  "
         if DEROG is None :
            return  " SVp Remplir les champs  "
         if DELINQ is None :
            return  " SVp Remplir les champs  "
         if CLAGE is None :
            return  " SVp Remplir les champs  "
         if NINQ is None :
            return  " SVp Remplir les champs  "
         if CLNO is None :
            return  " SVp Remplir les champs  "
         if DEBTINC is None :
            return  " SVp Remplir les champs  "
         if LOAN is None :
            return  " SVp Remplir les champs  "
         if MORTDUE is None :
            return  " SVp Remplir les champs  "

         df = np.array([LOAN, MORTDUE,VALUE,YOJ,DEROG,DELINQ,CLAGE,NINQ,CLNO,DEBTINC]).reshape(1,10)
        # df = pd.DataFrame(df)
        # res=np.array([1,0])
       #  ma= np.array([1,0,1,0,0,0,0,0])
        # mat1=pd.DataFrame((ma.reshape(1,8))
        # dff=pd.concat([df,mat1],axis=1)
         #mat=pd.DataFrame((res.reshape(1,2))

        #if(REASON=='HomeImp'):
           # res=np.array([0,1])
         #else
          #  res=np.array([1,0])

        #ds= pd.DataFrame(REASON)


#	LOAN	MORTDUE	VALUE	YOJ	DEROG	DELINQ	CLAGE	NINQ	CLNO	DEBTINC	REASON_DebtCon	REASON_HomeImp	JOB_Mgr	JOB_Office	JOB_Other	JOB_ProfExe	JOB_Sales	JOB_Self


         df = pd.DataFrame(df)
         mat= np.array([1,0,1,0,0,0,0,0])
         g=pd.DataFrame((mat.reshape(1,8)))

         dff=pd.concat([df,g],axis=1)

         if  data[1][1].predict(dff)==0:
            return "felicitation! un bon client"
         else :
            return "Mauvais client"
    return "Remplir les champs pour prédire client "



@app.callback(Output("output_msg_3","className"),[Input("output_msg_3","children")])
def change_color(input1):
    if input1.startswith(" SVp Remplir les champs  "):
        return "alert alert-warning text-center mt-4 "

    if input1.startswith("felicitation"):
        return "alert alert-success text-center mt-4"

    if input1.startswith("Mauvais"):
        return "alert alert-danger text-center mt-4"

    return "alert alert-primary text-center mt-4"

@app.callback(
#Output('table','data'),

 dash.dependencies.Output( component_id='body-div', component_property='children'),
  [Input("go","n_clicks")],
[
    State("bnq_selector","value"),
]  )


def update_graph(inp,data_name_selected):
 if inp is not None:

    if data_name_selected is None :

        data=[]
    if data_name_selected=='a' :
        dt_col_param = []
        for col in AM.columns:
            dt_col_param.append({"name": str(col), "id": str(col)})
        data=dash_table.DataTable(
            columns=dt_col_param,
            data=AM.to_dict('records'))
    if data_name_selected == 'g':
        dt_col_param = []
        for col in TW.columns:
            dt_col_param.append({"name": str(col), "id": str(col)})
        data=dash_table.DataTable(
            columns=dt_col_param,
            data=TW.to_dict('records'))
    if data_name_selected == 't':
        dt_col_param = []
        for col in GR.columns:
            dt_col_param.append({"name": str(col), "id": str(col)})
        data=dash_table.DataTable(
            columns=dt_col_param,
            data=GR.to_dict('records'))

    return data#make_table(data, 'table')


app.run_server(debug=False)