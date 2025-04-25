import { Routes, Route } from 'react-router-dom';
import TestComponent  from './components/TestComponent';

export default function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <Routes>
        <Route path="/" element={<TestComponent />} />
      </Routes>
    </div>
  );
}