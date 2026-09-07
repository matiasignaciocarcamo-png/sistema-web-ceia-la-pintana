import React from 'react';
import {BrowserRouter,Routes,Route,Navigate} from 'react-router-dom';
import Login from './pages/Login'; import Dashboard from './pages/Dashboard'; import Cursos from './pages/Cursos'; import Estudiantes from './pages/Estudiantes'; import Asistencia from './pages/Asistencia'; import Inventario from './pages/Inventario'; import Agenda from './pages/Agenda'; import Usuarios from './pages/Usuarios'; import Layout from './components/Layout';
const Private=({children})=>localStorage.getItem('token')?children:<Navigate to="/login" replace/>;
export default function App(){return <BrowserRouter><Routes>
<Route path="/login" element={<Login/>}/><Route element={<Private><Layout/></Private>}>
<Route index element={<Dashboard/>}/><Route path="cursos" element={<Cursos/>}/><Route path="estudiantes" element={<Estudiantes/>}/><Route path="asistencia" element={<Asistencia/>}/><Route path="inventario" element={<Inventario/>}/><Route path="agenda" element={<Agenda/>}/><Route path="usuarios" element={<Usuarios/>}/>
</Route><Route path="*" element={<Navigate to="/"/>}/></Routes></BrowserRouter>}
