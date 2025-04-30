import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import DatasetCreateForm from './components/DatasetCreateForm';
import DatasetList from './components/DatasetList';
import DatasetDetail from './components/DatasetDetail';
import ResourceCreateForm from './components/ResourceCreateForm';

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/datasets/:id" element={<DatasetDetail />} />
      <Route path="/datasets/create" element={<DatasetCreateForm />} />
      <Route path="/datasets/:id/resources/add" element={<ResourceCreateForm />} />
    </Routes>
  );
};

const Home = () => {
  return (
    <div>
      <h1>صفحه اصلی</h1>
      <Link to="/datasets/create">
        <button>افزودن دیتاست جدید</button>
      </Link>
      <DatasetList />
    </div>
  );
};

export default App;
