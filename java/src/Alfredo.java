package pastas;

public class Alfredo extends Pasta {
	private String _addOn;
	private boolean _cached = false;
	private String _dish = null;
	
	public Alfredo(String addOn) {
		_addOn = addOn;
	}
	public Alfredo(){
		this("Plain");
	}
	
	private void _updateCache() {
		if(_addOn == "Plain"){
			_dish = "Classic Alfredo";
			_cached = true;
		}
		else {
			_dish = _addOn + " Alfredo";
			_cached = true;
		}
	}
	
	public String getAddOn(){
		return _addOn;
	}
	
	public void setAddOn(String value) {
		if(value != _addOn) {
			_addOn = value;
			_cached = false;
		}
	}
	
	public String getDish() {
		if(!_cached) {
			_updateCache();
		}
		return _dish;
	}
}