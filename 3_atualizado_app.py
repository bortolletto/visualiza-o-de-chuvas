#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:44:49 2023

@author: felipe.bortolletto
"""

#bibliotecas
import pandas as pd 
import numpy as np 
from dash import dcc ,html , Dash
from dash.dependencies import Input, Output ,State
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from plotly.subplots import make_subplots

#%%


df_estacoes = pd.read_csv("./din_df_estacoes.csv", index_col='id_estacao', dtype={'id_estacao':int})

   


legenda = {
  '<10': '#e63f1a',
 '10-20': '#ff6600',
 '20-30': '#ff9900',
 '30-40': '#ffcc00',
 '40-60': '#f5e211',
 '60-80': '#ffff00',
 '80-100': '#ffff99',
 '100-140': '#b6fbab',
 '140-180': '#78f573',
 '180-220': '#35d23b',
 '220-260': '#11a010',
 '260-300': '#e9feff',
 '300-340': '#c3e0fe',
 '340-380': '#8da2ff',
 '380-420': '#4e5bff',
 '>420': '#0400f9',
 'NaN': 'black'}



classe_cores =    {'<10': ('#e63f1a',
        '<b>Código</b>: %{customdata[8]}' + \
         '<i><br>Estação</i>: %{customdata[1]}<br>'+ \
                     'Órgão: %{customdata[4]}<br>' + \
                     '<br><b><i>Total (mm)<i></b>: <b>%{customdata[0]:.1f}</b>' 
                         ),
     '10-20': ('#ff6600',
        '<b>Código</b>: %{customdata[8]}' + \
         '<i><br>Estação</i>: %{customdata[1]}<br>'+ \
                     'Órgão: %{customdata[4]}<br>' + \
                     '<br><b><i>Total (mm)<i></b>: <b>%{customdata[0]:.1f}</b>' 
                         ),
     '20-30': ('#ff9900',
        '<b>Código</b>: %{customdata[8]}' + \
         '<i><br>Estação</i>: %{customdata[1]}<br>'+ \
                     'Órgão: %{customdata[4]}<br>' + \
                     '<br><b><i>Total (mm)<i></b>: <b>%{customdata[0]:.1f}</b>' 
                         ),
     '30-40': ('#ffcc00',
        '<b>Código</b>: %{customdata[8]}' + \
         '<i><br>Estação</i>: %{customdata[1]}<br>'+ \
                     'Órgão: %{customdata[4]}<br>' + \
                     '<br><b><i>Total (mm)<i></b>: <b>%{customdata[0]:.1f}</b>' 
                         ),
     '40-60': ('#f5e211',
        '<b>Código</b>: %{customdata[8]}' + \
         '<i><br>Estação</i>: %{customdata[1]}<br>'+ \
                     'Órgão: %{customdata[4]}<br>' + \
                     '<br><b><i>Total (mm)<i></b>: <b>%{customdata[0]:.1f}</b>' 
                         ),
     '60-80': ('#ffff00',
        '<b>Código</b>: %{customdata[8]}' + \
         '<i><br>Estação</i>: %{customdata[1]}<br>'+ \
                     'Órgão: %{customdata[4]}<br>' + \
                     '<br><b><i>Total (mm)<i></b>: <b>%{customdata[0]:.1f}</b>' 
                         ),
     '80-100': ('#ffff99',
        '<b>Código</b>: %{customdata[8]}' + \
         '<i><br>Estação</i>: %{customdata[1]}<br>'+ \
                     'Órgão: %{customdata[4]}<br>' + \
                     '<br><b><i>Total (mm)<i></b>: <b>%{customdata[0]:.1f}</b>' 
                         ),
     '100-140': ('#b6fbab',
        '<b>Código</b>: %{customdata[8]}' + \
         '<i><br>Estação</i>: %{customdata[1]}<br>'+ \
                     'Órgão: %{customdata[4]}<br>' + \
                     '<br><b><i>Total (mm)<i></b>: <b>%{customdata[0]:.1f}</b>' 
                         ),
     '140-180': ('#78f573',
        '<b>Código</b>: %{customdata[8]}' + \
         '<i><br>Estação</i>: %{customdata[1]}<br>'+ \
                     'Órgão: %{customdata[4]}<br>' + \
                     '<br><b><i>Total (mm)<i></b>: <b>%{customdata[0]:.1f}</b>' 
                         ),
     '180-220': ('#35d23b',
        '<b>Código</b>: %{customdata[8]}' + \
         '<i><br>Estação</i>: %{customdata[1]}<br>'+ \
                     'Órgão: %{customdata[4]}<br>' + \
                     '<br><b><i>Total (mm)<i></b>: <b>%{customdata[0]:.1f}</b>' 
                         ),
     '220-260': ('#11a010',
        '<b>Código</b>: %{customdata[8]}' + \
         '<i><br>Estação</i>: %{customdata[1]}<br>'+ \
                     'Órgão: %{customdata[4]}<br>' + \
                     '<br><b><i>Total (mm)<i></b>: <b>%{customdata[0]:.1f}</b>' 
                         ),
     '260-300': ('#e9feff',
        '<b>Código</b>: %{customdata[8]}' + \
         '<i><br>Estação</i>: %{customdata[1]}<br>'+ \
                     'Órgão: %{customdata[4]}<br>' + \
                     '<br><b><i>Total (mm)<i></b>: <b>%{customdata[0]:.1f}</b>' 
                         ),
     '300-340': ('#c3e0fe',
        '<b>Código</b>: %{customdata[8]}' + \
         '<i><br>Estação</i>: %{customdata[1]}<br>'+ \
                     'Órgão: %{customdata[4]}<br>' + \
                     '<br><b><i>Total (mm)<i></b>: <b>%{customdata[0]:.1f}</b>' 
                         ),
     '340-380': ('#8da2ff',
        '<b>Código</b>: %{customdata[8]}' + \
         '<i><br>Estação</i>: %{customdata[1]}<br>'+ \
                     'Órgão: %{customdata[4]}<br>' + \
                     '<br><b><i>Total (mm)<i></b>: <b>%{customdata[0]:.1f}</b>' 
                         ),
     '380-420': ('#4e5bff',
        '<b>Código</b>: %{customdata[8]}' + \
         '<i><br>Estação</i>: %{customdata[1]}<br>'+ \
                     'Órgão: %{customdata[4]}<br>' + \
                     '<br><b><i>Total (mm)<i></b>: <b>%{customdata[0]:.1f}</b>' 
                         ),
     '>420': ('#0400f9',
        '<b>Código</b>: %{customdata[8]}' + \
         '<i><br>Estação</i>: %{customdata[1]}<br>'+ \
                     'Órgão: %{customdata[4]}<br>' + \
                     '<br><b><i>Total (mm)<i></b>: <b>%{customdata[0]:.1f}</b>' 
                         ),
     'NaN': ('black',
        '<b>Código</b>: %{customdata[8]}' + \
         '<i><br>Estação</i>: %{customdata[1]}<br>'+ \
                     'Órgão: %{customdata[4]}<br>' + \
                     '<br><b><i>Total (mm)<i></b>: <b>%{customdata[0]:.1f}</b>' 
                         ),
         }

 
 
def classifica_inmet_climatologia(x):
    if np.isnan(x):
        return 'NaN'
    if x <= 10:
        return '<10'
    if x <= 20:
        return '10-20'
    if x <= 30:
        return '20-30'
    if x <= 40:
        return '30-40'
    if x <= 60:
        return '40-60'
    if x <= 80:
        return '60-80'
    if x <= 100:
        return '80-100'
    if x <= 140:
        return '100-140'
    if x <= 180:
        return '140-180'
    if x <= 220:
        return '180-220'
    if x <= 260:
        return '220-260'
    if x <= 300:
        return '260-300'
    if x <= 340:
        return '300-340'
    if x <= 380:
        return '340-380'
    if x <= 420:
        return '380-420'
    if x > 420:
        return '>420'
    


blackbold={'color':'black', 'font-weight': 'bold'}



dct_check = [
{'label': 'IAT  ', 'value': 'IAT'},
{'label': 'Simepar  ',
 'value': 'Simepar'},
{'label': 'Cemaden  ',
 'value': 'Cemaden'},{'label':'Sanepar ','value':'Sanepar'},

 {'label': 'PCJ  ',
  'value': 'PCJ'},
 {'label': 'Elejor  ', 'value': 'ELEJOR'},
 {'label': 'Inmet  ', 'value': 'Inmet'},
 {'label': 'Klabin  ', 'value': 'Klabin'},
 {'label': 'Mauá  ', 'value': 'Mauá'},
 {'label': 'Andreoli  ', 'value': 'Arturo Andreoli'},
 {'label': 'Cavernoso II  ', 'value': 'Cavernoso II'},
 {'label': 'São Francisco  ', 'value': 'São Francisco'},
 {'label': 'Outros  ', 'value': 'Outros'},
]
   
rename_columns = {'CEMADEN': 'Cemaden',
 'Epagri/Ciram': 'Outros',
 'Instituto Nacional de Meteorologia': 'Inmet',
 'LIGHT': 'Outros',
 'Instituto Água e Terra': 'IAT',
 'Sistema Meteorológico do Paraná': 'Simepar',
 'Projeto Lactec': 'Outros',
 'Duke Energy': 'Outros',
 'Instituto Agronômico do Paraná ': 'Outros',
 'Superintendência de Recursos Hídricos ': 'Outros',
 'Consórcio Energético Cruzeiro do Sul - Usina de Mauá': 'Mauá',
 'PCJ -Sistema de Alerta a Inundações de São Paulo': 'PCJ',
 'Centrais Elétricas do Rio Jordão': 'Outros',
 'Estações Orbcomm da Copel': 'Outros',
 'PCH Cavernoso II': 'Cavernoso II',
 'Constremac': 'Outros',
 'Departamento de Estradas de Rodagem': 'Outros',
 'TESTE': 'Outros',
 'Companhia de Saneamento do Paraná': 'Sanepar',
 'Klabin': 'Klabin',
 'Petrobrás': 'Outros',
 'PCH Energética Arturo Andreoli': 'Arturo Andreoli',
 'PCH Novo Horizonte': 'Outros',
 'Companhia Hidro Elétrica do São Francisco': 'São Francisco'}


df_estacoes.name_orgao.replace(rename_columns,inplace = True)

#%% elemetos 
chuva_estacoes = pd.read_csv("./din_df_chuva_estacoes.csv",parse_dates=['datetime'], index_col='datetime')

t_inicio = chuva_estacoes.index[0]

t_fim=chuva_estacoes.index[-1]


app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY])

all_for_one = dbc.Button("Todos/Nenhum",
                         id = "all-or-none",
                         n_clicks = 3,
                         size = "me-1",
                         className = "border rounded border-primary border-opacity-25 w-25 border border-3")
                                        
checklist = dcc.Checklist(id = "orgao",

                  options = dct_check,inline = True,
                   value = [],
                  inputStyle={"margin-right": "5px","margin-left": "5px"},
                  style={"margin-left": 25}
        )
checkilist_ativos = dcc.Checklist( id ="ativos",
                                  options = [{"label":"Incluso","value":"s"},
                                            {"label":"Não inclusos","value":"n"}],
                                  value   = ["s"],
                                                    inputStyle={"margin-right": "5px","margin-left": "5px"},
                                                    style={"margin-left": 25}             
    )
input_box = dcc.Input(id = "input_{}".format("number"),type = "number",debounce=True)


#------------------------ html.graph ------------------------------
mapa =   dcc.Graph(id = "figura", figure={},style={"height": 650,"margin-left": 15})   

grafico = dcc.Graph(id="grafico",figure= {},style={"height": 650}) 

#------------------------ html.label ------------------------------
checklist_title = html.Label(children=['Orgão: '], style=blackbold)
input_title = html.Label(children=['Escolha uma estação: '], style=blackbold)

#------------------------ dcc.store -------------------------------
banco = dcc.Store(
        id = "store_data",data = [],storage_type ='memory'
    )


#%%




app.layout = dbc.Container([
    dbc.Row([
        
        dbc.Col(
            
    html.H1("Monitoramento de chuvas no Paraná - SIMEPAR",className="border border-4 ",style={"backgroundColor":"dee2e6"}),
    )
        
        ]),
    
    html.Br(),
    dbc.Row([
        dbc.Col([checklist_title,
                 html.Div(all_for_one),
                 checklist,
                 html.Div([
                 # html.Br(),
                 html.Label("Siprec+:",style={"backgroundColor":"dee2e6","margin-left": 25}),checkilist_ativos],className = "border-top",style=blackbold),]),
        dbc.Col([input_title,input_box],),
        ]),
    html.Br(),
    html.Div([
    dbc.Row([
        dbc.Col(mapa,width =6,xs = 6,md = 6, lg = 6, xxl = 6,sm = 6,xl = 6),
        
        dbc.Col(grafico,width =6,xs = 6,md = 6, lg = 6, xxl = 6,sm = 6,xl = 6)
        ])
    ],style = {"backgroundColor":"#dee2e6"} ),
    banco,
    ],style={'backgroundColor':'#dee2e6'} ,fluid = True)

   

#%% 



@app.callback(
    Output("orgao","value"),
      [Input("all-or-none","n_clicks")],
      [State("orgao","options")]
    )
def select_all_none(all_selected, options):
    if all_selected %2 ==0: 
        all_or_none = []
        all_or_none = [option["value"] for option in options if all_selected]
    elif all_selected ==3:
        all_or_none = ["Simepar","IAT"]
    else:
        all_or_none =[]
    return all_or_none



#%% 1 callback
@app.callback(
    [Output("figura","figure"),
    Output("store_data","data"),
    Output("input_{}".format("number"),"value"),
    ],
    [Input("orgao","value"),
     Input("input_{}".format("number"),"value"),
     Input("ativos","value")
     ]
)

def grafico(org,cod_input,ativo_):
    
    

    
    df_mes = pd.read_csv("./din_df_chuva_estacoes.csv",parse_dates=['datetime'], index_col='datetime')
    df_mes.columns=df_mes.columns.map(int)
    
    
    df_mes = df_mes.sum(axis=0,min_count=1).rename("Total").to_frame()
    df_mes.index = df_mes.index.astype(int)
    df_mes = pd.merge(df_mes,df_estacoes,how="inner",left_index=True,right_index=True)
    
    
    
    df_mes.drop(columns = [ 'stationtypeId', 'collectId', 'organizationId',
           'cityId', 'startoperation', 'installationdate',
           'altitude', 'endoperation', 'id_orgao', ],inplace = True)
    
    df_mes['Classe'] = df_mes.apply(lambda x: classifica_inmet_climatologia(x['Total']), axis=1) 
    if ativo_:
        if len(ativo_) == 1:
            df_mes = df_mes.loc[df_mes.smais == ativo_[0]]
 
        elif len(ativo_)==2:
            df_mes = df_mes

    else: 
        df_mes = df_mes.loc[(df_mes.smais == "nothing_at_all")]
        
    # df_mes['Classe'] = df_mes.apply(lambda x: classifica_inmet_climatologia(x['Total']), axis=1) 
    if cod_input: 
        
        dx= df_mes[df_mes.index == cod_input]
        
        df_mes_classe =pd.DataFrame(dx)
        df_mes_classe["codigo"] = dx.index
        df_mes_classe["cor"] = np.nan
        df_mes_classe["hovertemplate"]=np.nan
        
        
        for chavin in classe_cores:
            df_mes_classe.loc[df_mes_classe.Classe == chavin,"cor"] = classe_cores[chavin][0]
            df_mes_classe.loc[df_mes_classe.Classe == chavin,"hovertemplate"] = classe_cores[chavin][1]
            
        
    else:
        dx = df_mes[df_mes["name_orgao"].isin(org)]
        #[(df_mes["name_orgao"].isin(org))]   
        
        df_mes_classe =pd.DataFrame(dx)
        df_mes_classe["codigo"] = dx.index
        df_mes_classe["cor"] = np.nan
        df_mes_classe["hovertemplate"]=np.nan
        
        for chavin in classe_cores:
            df_mes_classe.loc[df_mes_classe.Classe == chavin,"cor"] = classe_cores[chavin][0]
            df_mes_classe.loc[df_mes_classe.Classe == chavin,"hovertemplate"] = classe_cores[chavin][1]

    
    #-------------------------------- plot ---------------------------------
    fig = go.Figure() 
    
    for classe,cor in zip (legenda.keys(),legenda.values()):
        df_mes_classe_copy = df_mes_classe[df_mes_classe["Classe"] == classe]   
        fig.add_trace(go.Scattermapbox(
            lat = df_mes_classe_copy['latitude'],
            lon = df_mes_classe_copy['longitude'],
            customdata = df_mes_classe_copy,
            mode = 'markers',
            name =  classe,
            
            
            hoverinfo = 'text',
            hovertext = df_mes_classe_copy['Total'],
            hovertemplate = df_mes_classe_copy["hovertemplate"], 
            showlegend=True,
            marker = go.scattermapbox.Marker(
                size = 15,
                color = cor,
                opacity = 1,
                ),
            )
        )

        fig.update_layout(
        legend_title_text='Acumulado(mm)',
        autosize = True,
        margin=dict(l=20, r=20, t=30, b=20),
        legend=dict(
            y=0.99,
            xanchor="left",
            x=0.01),
        hovermode = 'closest',
        paper_bgcolor="LightSteelBlue",
        
        font=dict(
        family="Courier New, monospace",
        size=13),
        
        mapbox = dict(
            style ='open-street-map', 
            center =  {'lon':-51.35, 'lat':-24.62},
            zoom = 6,
        ), 
    )

    return fig,dx.to_dict("records"),""



#%% segundo callback ----------------------------------------------------------


@app.callback(Output("grafico","figure"),
              Input("store_data","data"),
              Input("figura","clickData"))

def criando_grafico(dx,clickData):
    chuva_estacoes = pd.read_csv("./din_df_chuva_estacoes.csv",parse_dates=['datetime'], index_col='datetime')
    t_inicio = chuva_estacoes.index[0]

    t_fim=chuva_estacoes.index[-1]
    
    dff = pd.DataFrame(dx)
   

    if clickData:
            
            fig =  make_subplots(specs=[[{"secondary_y": True}]])
            
            clicado = dff.loc[(dff.latitude == clickData["points"][0]["lat"]) & (dff.longitude == clickData["points"][0]["lon"])]
            codigo = clicado.values[0][8]
            nome = clicado.values[0][1]
            
            df_grafico =pd.DataFrame(chuva_estacoes[str(codigo)]).reset_index()
            
            df_grafico["nulos"] = 0
            df_grafico.fillna(-9999 ,inplace = True)
            df_grafico["nulos"] = df_grafico[[str(codigo),"nulos"]].apply(lambda x: 1 if x[str(codigo)] ==-9999 else 0,axis = 1)
            df_grafico.loc[df_grafico[str(codigo)]==-9999,str(codigo)] = np.nan
            for i in df_grafico.index:
                if i == 0:
                    df_grafico.loc[df_grafico.index == 0,"somatorio"] = df_grafico.loc[df_grafico.index==0,str(codigo)].values[0]
                else:
                    df_grafico.loc[df_grafico.index == i,"somatorio"] = df_grafico[str(codigo)][:i+1].sum()
                    
            fig.add_trace(go.Bar(x =df_grafico.datetime  , y =df_grafico[str(codigo)] ,name = "Diário",marker_color = "blue"))
            fig.add_trace(go.Scatter(x = df_grafico.datetime,y = df_grafico["somatorio"],name = "Acumulado",marker_color = "red"),secondary_y = True)
            fig.add_trace(go.Bar(x =df_grafico.datetime  , y =df_grafico["nulos"] ,name = "NAN",marker_color = "yellow"))
            
            fig.update_layout(
                    paper_bgcolor="LightSteelBlue",
                    margin=dict(l=20, r=20, t=30, b=20),
                    title={"text" : f"{nome}({codigo})<br><sup>{t_inicio.day:02d}/{t_inicio.month:02d}/{t_inicio.year} 10 às {t_fim.strftime('%d/%m/%Y %H')} (UTC)</sup> ",
                           'y':0.98,
                           'x':0.5,},
                    font=dict(
                      family="Courier New, monospace",
                      size=11),

                    hoverdistance=100,
                    hovermode="x",
                     xaxis=dict(

                         title="Data",
                         linecolor="#BCCCDC",  
                         showgrid=False ,
                         
                        ),
                     yaxis=dict(
                        title="mm/dia*",  
                        linecolor="#BCCCDC", 
                        showgrid=False,
                     ),
                        
                )
            fig.add_annotation(dict(font=dict(color='black',size=10),
                                        x=0.5,
                                        y=-0.11,
                                        showarrow=False,
                                        text="*Para a agregação diária, considerou-se EoD (end of day) = 10:00:00 UTC",
                                        textangle=0,
                                        xanchor='left',
                                        xref="paper",
                                        yref="paper"))
                
            
            return fig 
    else:
          fig = make_subplots(specs=[[{"secondary_y": True}]])
        
          df_grafico =pd.DataFrame(chuva_estacoes[str(24055072)]).reset_index()
          df_grafico["nulos"] = 0
          df_grafico.fillna(-9999 ,inplace = True)
          df_grafico["nulos"] = df_grafico[["24055072","nulos"]].apply(lambda x: 1 if x["24055072"] ==-9999 else 0,axis = 1)
          df_grafico.loc[df_grafico["24055072"]==-9999,"24055072"] = np.nan
          for i in df_grafico.index:
              
              if i == 0:
                  df_grafico.loc[df_grafico.index == 0,"somatorio"] = df_grafico.loc[df_grafico.index==0,"24055072"].values[0]
              else:
                  df_grafico.loc[df_grafico.index == i,"somatorio"] = df_grafico["24055072"][:i+1].sum()
          
          fig.add_trace(go.Bar(x =df_grafico.datetime  , y =df_grafico[str(24055072)] ,name = "Diário",marker_color = "blue"))
          fig.add_trace(go.Scatter(x = df_grafico.datetime,y = df_grafico["somatorio"],name = "Acumulado",marker_color = "red"),secondary_y = True)
          fig.add_trace(go.Bar(x =df_grafico.datetime  , y =df_grafico["nulos"] ,name = "NAN",marker_color = "yellow"))

          fig.update_layout(
                  paper_bgcolor="LightSteelBlue",
                  margin=dict(l=20, r=20, t=30, b=20),
                  title={"text" : f"Chuva: UHPV Barramento- 24055072<br><sup> {t_inicio.day:02d}/{t_inicio.month:02d}/{t_inicio.year} 10 às {t_fim.strftime('%d/%m/%Y %H')} (UTC)</sup> ",
                         'y':0.98,
                         'x':0.5,},
                  font=dict(
                    family="Courier New, monospace",
                    size=11),
                  hoverdistance=100,
                  hovermode="x",
                   xaxis=dict(

                       title="Data",
                       linecolor="#BCCCDC",  
                       showgrid=False ,
                       
                      ),
                   yaxis=dict(
                      title="mm/dia*",  
                      linecolor="#BCCCDC", 
                      showgrid=False,
                   ),
                   )
                   # plot_bgcolor="#FFF"      

          fig.add_annotation(dict(font=dict(color='black',size=10),
                                        x=0.5,
                                        y=-0.11,
                                        showarrow=False,
                                        text="*Para a agregação diária, considerou-se EoD (end of day) = 10:00:00 UTC",
                                        textangle=0,
                                        xanchor='left',
                                        xref="paper",
                                        yref="paper"))

        
        
        
          return fig
        
    


    
    
    


if __name__ == '__main__':
    app.run_server( port = '8765', debug=True)
    #app.run_server( host = 'vmhidro2.simeparnet',port = '8000', debug=False)
    
